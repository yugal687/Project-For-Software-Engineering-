# Generated by Django 5.1.1 on 2024-11-27 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0027_alter_professor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='user',
        ),
    ]
