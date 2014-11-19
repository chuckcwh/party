# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='groups_user', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
