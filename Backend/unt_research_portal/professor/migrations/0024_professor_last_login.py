# Generated by Django 5.1.1 on 2024-11-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0023_remove_professor_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
