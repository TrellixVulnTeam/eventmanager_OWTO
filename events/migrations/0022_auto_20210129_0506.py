# Generated by Django 3.1.5 on 2021-01-29 05:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_auto_20210128_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='angelegt am')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='geändert am')),
                ('name', models.CharField(max_length=255)),
                ('firstname', models.CharField(blank=True, max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('label', models.CharField(max_length=64)),
                ('attend_status', models.CharField(choices=[('registered', 'angemeldet'), ('waiting', 'Warteliste'), ('attending', 'nimmt teil'), ('absent', 'nicht erschienen'), ('cancelled', 'abgesagt')], max_length=10)),
                ('mail_to_admin', models.BooleanField(default=False, verbose_name='m > admin')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='events.event')),
            ],
            options={
                'unique_together': {('event', 'name')},
            },
        ),
        migrations.DeleteModel(
            name='EventMemberAnonymous',
        ),
    ]
