# Generated by Django 3.1.5 on 2021-05-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0064_event_pub_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmember',
            name='via_form',
            field=models.BooleanField(default=False, verbose_name='AF'),
        ),
        migrations.AlterField(
            model_name='eventmember',
            name='attend_status',
            field=models.CharField(choices=[('registered', 'angemeldet'), ('waiting', 'Warteliste'), ('attending', 'nimmt teil'), ('absent', 'nicht erschienen'), ('cancelled', 'abgesagt')], max_length=10, verbose_name='Status'),
        ),
    ]
