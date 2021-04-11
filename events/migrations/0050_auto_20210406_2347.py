# Generated by Django 3.1.5 on 2021-04-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0049_auto_20210406_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventagenda',
            options={'ordering': ('position',), 'verbose_name': 'Programm', 'verbose_name_plural': 'Programme'},
        ),
        migrations.RemoveField(
            model_name='eventagenda',
            name='order',
        ),
        migrations.AddField(
            model_name='eventagenda',
            name='position',
            field=models.PositiveSmallIntegerField(help_text='Reihenfolge der Programme in der Anezige', null=True, verbose_name='Reihenfolge'),
        ),
    ]