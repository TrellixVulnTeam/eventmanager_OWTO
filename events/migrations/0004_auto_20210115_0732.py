# Generated by Django 3.1.5 on 2021-01-15 07:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210115_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='prerequisites',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='Voraussetzungen'),
        ),
    ]
