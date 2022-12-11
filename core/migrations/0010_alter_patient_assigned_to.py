# Generated by Django 4.1.3 on 2022-11-11 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_remove_patient_assigned_to_patient_assigned_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="assigned_to",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]