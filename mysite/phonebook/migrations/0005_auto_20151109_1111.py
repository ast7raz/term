# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_auto_20150331_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='base_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='base_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partner',
            name='base_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
