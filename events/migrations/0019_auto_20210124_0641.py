# Generated by Django 3.1.5 on 2021-01-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_event_students_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
