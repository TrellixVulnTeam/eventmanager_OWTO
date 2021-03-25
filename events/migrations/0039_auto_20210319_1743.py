# Generated by Django 3.1.5 on 2021-03-19 17:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_auto_20210319_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='speaker',
        ),
        migrations.CreateModel(
            name='EventSpeakerThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='angelegt am')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='geändert am')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('eventspeaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventspeaker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='speaker',
            field=models.ManyToManyField(through='events.EventSpeakerThrough', to='events.EventSpeaker', verbose_name='Referent*innen'),
        ),
    ]