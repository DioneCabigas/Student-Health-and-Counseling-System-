# Generated by Django 5.1.2 on 2024-12-10 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0042_rename_user_patient_userprofile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='studentID',
            new_name='userID',
        ),
    ]
