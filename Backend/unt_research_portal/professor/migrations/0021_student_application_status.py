# Generated by Django 5.1.3 on 2024-11-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0020_rename_application_student_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
