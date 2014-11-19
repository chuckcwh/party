# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0002_auto_20141119_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='groups_user', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='group',
            field=models.ManyToManyField(related_name='parties_group', null=True, to='partyApp.Group', blank=True),
            preserve_default=True,
        ),
    ]
