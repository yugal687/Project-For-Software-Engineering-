# Generated by Django 5.1.1 on 2024-12-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_student_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='resume_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
