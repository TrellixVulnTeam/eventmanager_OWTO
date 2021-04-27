# Generated by Django 3.1.5 on 2021-04-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0056_event_first_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='moodle_standard_passwort',
            field=models.CharField(default='VfllMoodle123#', max_length=24, verbose_name='Moodle Standard-Passwort'),
        ),
        migrations.AlterField(
            model_name='event',
            name='moodle_new_user_flag',
            field=models.BooleanField(default=False, help_text='Hier kann für den Kurs festgelegt werden, ob neue Moodle-User die automatische Begrüßungsmail bekommen (default=False).', verbose_name='Autom. E-Mail an neue Moodle-User'),
        ),
    ]
