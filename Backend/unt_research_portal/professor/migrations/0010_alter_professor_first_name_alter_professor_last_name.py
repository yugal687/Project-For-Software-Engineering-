# Generated by Django 5.1.1 on 2024-11-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0009_professor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='professor',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]