# Generated by Django 5.1.1 on 2024-11-27 02:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0025_professor_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professor_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
