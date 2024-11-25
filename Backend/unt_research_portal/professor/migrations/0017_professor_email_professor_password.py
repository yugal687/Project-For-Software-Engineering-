# Generated by Django 5.1.1 on 2024-11-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0016_remove_professor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='email',
            field=models.EmailField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
    ]
