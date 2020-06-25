from dateparser import parse
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone
from simple_history.models import registered_models

# Instances which are created at run-time, referencing config-time models
# eg. Answers are created at run-time by users and referencing Question
RELATED_HISTORICAL_MODELS = {
    "Answer": {"question__type__isnull": True},
    "Document": {"form__name__isnull": True},
    "DynamicOption": {"question__type__isnull": True},
}


class Command(BaseCommand):
    """Cleanup historical records."""

    help = "Cleanup historical records."

    def add_arguments(self, parser):
        parser.add_argument("--force", dest="force", default=False, action="store_true")
        parser.add_argument(
            "-k",
            "--keep",
            dest="keep",
            default="1 year",
            help=(
                "Duration we want to keep the records. "
                "E.g. '6 months', '1 year'. Uses dateparser."
            ),
        )
        parser.add_argument(
            "-d",
            "--dangling",
            dest="dangling",
            default=False,
            action="store_true",
            help=(
                "Remove records missing a related instance, e.g. HistoricalAnswer missing the Question it relates to."
                "Caution: This does not respect the --keep option but removes ALL such instances."
            ),
        )

    def handle(self, *args, **options):
        force = options["force"]
        dangling = options["dangling"]
        keep = options["keep"]

        if keep:
            keep = timezone.make_aware(parse(keep))

        for model in registered_models.values():
            qs = model.history.all()
            _filter = Q()

            if keep is not None:
                _filter = Q(history_date__lt=keep)

            if dangling and model.__name__ in RELATED_HISTORICAL_MODELS:
                _filter |= Q(**RELATED_HISTORICAL_MODELS[model.__name__])

            qs = qs.filter(_filter)

            action_str = "Deleting" if force else "Would delete"
            self.stdout.write(
                f'{action_str} {qs.count()} historical records from model "{model.__name__}"'
            )
            if force:
                qs.delete()
