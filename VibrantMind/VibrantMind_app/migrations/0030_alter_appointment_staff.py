# Generated by Django 5.1.2 on 2024-11-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0029_alter_appointment_appointment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='staff',
            field=models.CharField(blank=True, choices=[('Health Staff', 'Health Staff'), ('Counceling Staff', 'Counceling Staff')], max_length=100),
        ),
    ]
