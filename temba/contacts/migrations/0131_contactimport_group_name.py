# Generated by Django 2.2.19 on 2021-04-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0130_auto_20210105_2247"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactimport",
            name="group_name",
            field=models.CharField(max_length=64, null=True),
        ),
    ]