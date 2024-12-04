# Generated by Django 5.1.3 on 2024-12-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_studentapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='recommendation_letter',
            field=models.FileField(blank=True, null=True, upload_to='coi_documents/recommendation_letters/'),
        ),
        migrations.AddField(
            model_name='studentapplication',
            name='student_unt_id',
            field=models.FileField(blank=True, null=True, upload_to='coi_documents/student_ids/'),
        ),
        migrations.AddField(
            model_name='studentapplication',
            name='transcript',
            field=models.FileField(blank=True, null=True, upload_to='coi_documents/transcripts/'),
        ),
    ]