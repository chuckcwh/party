# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('partyImage', models.ImageField(default=b'party_pictures/default-party-photo.jpg', null=True, upload_to=b'party_pictures', blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time', models.DateTimeField()),
                ('maxPpl', models.SmallIntegerField(null=True, blank=True)),
                ('minAge', models.SmallIntegerField(null=True, blank=True)),
                ('maxAge', models.SmallIntegerField(null=True, blank=True)),
                ('targetSex', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
