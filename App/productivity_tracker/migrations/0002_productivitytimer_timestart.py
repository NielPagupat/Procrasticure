# Generated by Django 5.1.4 on 2024-12-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivitytimer',
            name='timeStart',
            field=models.TimeField(null=True),
        ),
    ]
