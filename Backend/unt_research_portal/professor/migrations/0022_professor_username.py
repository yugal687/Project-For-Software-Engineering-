# Generated by Django 5.1.1 on 2024-11-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0021_professor_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]