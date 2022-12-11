# Generated by Django 4.0.5 on 2022-11-12 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_visits_visit_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visits',
            name='diagnosis',
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField(default='No Diagnosis')),
                ('medical_history', models.TextField(default='No medical history')),
                ('doc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.documents')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.patient', to_field='patient_id')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('visit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.visits')),
            ],
        ),
    ]