# Generated by Django 5.1.3 on 2024-12-04 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coi_staff', '0003_remove_coistaff_last_login'),
        ('professor', '0029_student_application_resume_score'),
        ('students', '0009_studentapplication_resume_score_alter_student_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoiDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent_form', models.FileField(blank=True, null=True, upload_to='coi_documents/consent_forms/')),
                ('student_uni_id', models.FileField(blank=True, null=True, upload_to='coi_documents/student_ids/')),
                ('transcript', models.FileField(blank=True, null=True, upload_to='coi_documents/transcripts/')),
                ('recommendation_letter', models.FileField(blank=True, null=True, upload_to='coi_documents/recommendation_letters/')),
                ('nda', models.FileField(blank=True, null=True, upload_to='coi_documents/ndas/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('research_opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coi_documents', to='professor.researchopportunity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coi_documents', to='students.student')),
            ],
        ),
    ]
