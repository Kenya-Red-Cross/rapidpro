# Generated by Django 2.2.10 on 2020-08-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0112_last_seen_on_sys_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="status",
            field=models.CharField(
                choices=[("A", "Active"), ("B", "Blocked"), ("S", "Stopped"), ("V", "Archived")],
                default="A",
                max_length=1,
                null=True,
            ),
        )
    ]
