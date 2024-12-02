# Generated by Django 4.2.15 on 2024-12-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caluma_workflow', '0033_workitem_indexes'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='workitem',
            index=models.Index(fields=['created_at'], name='caluma_work_created_c87fd3_idx'),
        ),
        migrations.AddIndex(
            model_name='workitem',
            index=models.Index(fields=['deadline'], name='caluma_work_deadlin_3d2f3c_idx'),
        ),
    ]
