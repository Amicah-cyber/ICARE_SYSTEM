# Generated by Django 4.0.5 on 2022-11-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='annual_income',
        ),
    ]
