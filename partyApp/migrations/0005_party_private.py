# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partyApp', '0004_auto_20141119_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='private',
            field=models.CharField(default='Public', max_length=20),
            preserve_default=False,
        ),
    ]
