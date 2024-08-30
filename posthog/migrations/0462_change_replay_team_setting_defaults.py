# Generated by Django 4.2.14 on 2024-08-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0461_alter_externaldatasource_source_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="capture_console_log_opt_in",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="capture_performance_opt_in",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]