# Generated by Django 5.1.3 on 2024-12-04 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coi_staff', '0007_rename_status_coidocuments_onboarding_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coidocuments',
            name='consent_form',
        ),
        migrations.RemoveField(
            model_name='coidocuments',
            name='nda_acknowledged',
        ),
    ]