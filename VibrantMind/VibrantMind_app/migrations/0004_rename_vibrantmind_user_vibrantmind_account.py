# Generated by Django 5.1.2 on 2024-11-03 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0003_rename_user_vibrantmind_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VibrantMind_User',
            new_name='VibrantMind_Account',
        ),
    ]
