# Generated by Django 5.1.4 on 2024-12-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity_tracker', '0002_productivitytimer_timestart'),
    ]

    operations = [
        migrations.AddField(
            model_name='productivitytimer',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='productivitytimer',
            name='taskname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productivitytimer',
            name='timeEnd',
            field=models.TimeField(null=True),
        ),
    ]