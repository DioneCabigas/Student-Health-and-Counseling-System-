# Generated by Django 5.1.2 on 2024-12-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0037_alter_userprofile_age_alter_userprofile_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]
