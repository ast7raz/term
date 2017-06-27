# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duble_event', '0008_auto_20170623_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_config',
            name='transparent',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_config',
            name='volume',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
    ]
