# Generated by Django 5.1.3 on 2024-11-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='certifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='github_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='linked_in_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='portfolio_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_profile_pics/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='student_resumes/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
