# Generated by Django 2.2.4 on 2019-10-25 20:24

from django.db import migrations


def noop(apps, schema_editor):  # pragma: no cover
    pass


def fix_none_days(apps, schema_editor):  # pragma: no cover
    Schedule = apps.get_model("schedules", "Schedule")
    updated = Schedule.objects.filter(repeat_days_of_week__in=("None", "NaN")).update(repeat_days_of_week=None)
    if updated:
        print(f"fixed {updated} schedules with invalid day values")


class Migration(migrations.Migration):

    dependencies = [("schedules", "0012_auto_20190930_1347")]

    operations = [migrations.RunPython(fix_none_days, noop)]