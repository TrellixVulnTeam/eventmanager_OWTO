# Generated by Django 3.1.5 on 2022-06-25 07:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0105_auto_20220624_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pdf_file',
            field=models.FileField(blank=True, upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='eventhighlight',
            name='event',
            field=models.ForeignKey(limit_choices_to={'first_day__gte': datetime.date(2022, 6, 25), 'pub_status': 'PUB'}, on_delete=django.db.models.deletion.CASCADE, related_name='highlight', to='events.event'),
        ),
    ]
