# Generated by Django 5.1.2 on 2024-12-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VibrantMind_app', '0046_remove_prescription_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date_prescribed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
