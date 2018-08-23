# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 15:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("label", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("checkbox", "checkbox"),
                            ("number", "number"),
                            ("radio", "radio"),
                            ("textarea", "textarea"),
                            ("text", "text"),
                        ],
                        max_length=10,
                    ),
                ),
                ("is_required", models.TextField()),
                ("is_hidden", models.TextField()),
                (
                    "configuration",
                    django.contrib.postgres.fields.jsonb.JSONField(default={}),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
    ]
