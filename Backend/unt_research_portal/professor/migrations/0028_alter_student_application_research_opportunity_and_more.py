# Generated by Django 5.1.3 on 2024-12-03 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0027_student_application_status'),
        ('students', '0007_student_applied_at_student_resume_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_application',
            name='research_opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_applications', to='professor.researchopportunity'),
        ),
        migrations.AlterField(
            model_name='student_application',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_applications', to='students.student'),
        ),
    ]