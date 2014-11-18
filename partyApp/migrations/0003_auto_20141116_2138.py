# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0002_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='owner',
            field=models.ForeignKey(related_name='parties', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='party',
            name='maxAge',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='maxPpl',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='minAge',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
