# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0002_auto_20150331_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='keys',
            name='base_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
