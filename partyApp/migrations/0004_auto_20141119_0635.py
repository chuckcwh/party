# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0003_auto_20141119_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='host',
        ),
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.RemoveField(
            model_name='groupmsg',
            name='author',
        ),
        migrations.RemoveField(
            model_name='groupmsg',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupMsg',
        ),
        migrations.RemoveField(
            model_name='party',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='party',
            name='participants',
            field=models.ManyToManyField(related_name='parties_participants', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
