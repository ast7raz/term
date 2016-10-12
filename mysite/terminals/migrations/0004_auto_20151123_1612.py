# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0003_keys_base_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='keys',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keys',
            name='blocked',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='keys',
            name='admin',
            field=models.CharField(default=b'', max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='keys',
            name='ip',
            field=models.IPAddressField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='keys',
            name='version',
            field=models.CharField(default=b'', max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
