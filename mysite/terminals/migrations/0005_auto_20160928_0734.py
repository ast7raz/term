# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0004_auto_20151123_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keys',
            options={'permissions': (('Averange', 'Averange'),)},
        ),
        migrations.AddField(
            model_name='keys',
            name='date_last_online',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keys',
            name='machine_id',
            field=models.CharField(default=b'', max_length=35, blank=True),
            preserve_default=True,
        ),
    ]
