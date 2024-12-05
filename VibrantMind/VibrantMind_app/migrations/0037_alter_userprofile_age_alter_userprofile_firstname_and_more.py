# Generated by Django 5.1.2 on 2024-12-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0036_remove_patient_age_remove_patient_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='middleName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='studentID',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('staff', 'Staff')], max_length=50, null=True),
        ),
    ]
