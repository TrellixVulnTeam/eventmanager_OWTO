# Generated by Django 3.1.5 on 2021-04-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0046_auto_20210327_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='moodle_new_user_flag',
            field=models.BooleanField(default=False, help_text='Hier kann für den Kurs festgelegt werden, ob neue Moodle-User die automatische Begrüßungsmail bekommen (default=False).', verbose_name='E-Mail an neue Moodle-User'),
        ),
        migrations.AlterField(
            model_name='eventcategory',
            name='singular',
            field=models.CharField(blank=True, help_text='wird im Frontend als Kategorie angezeigt', max_length=255, null=True),
        ),
    ]
