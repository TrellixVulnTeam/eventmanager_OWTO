# Generated by Django 3.1.5 on 2021-07-26 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0073_auto_20210726_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmember',
            name='mv_check',
        ),
        migrations.RemoveField(
            model_name='eventmember',
            name='zw_check',
        ),
    ]