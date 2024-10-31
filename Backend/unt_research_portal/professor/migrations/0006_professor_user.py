# Generated by Django 5.1.1 on 2024-10-24 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_remove_professor_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='professor_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
