# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0006_parser_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='parser_users',
            name='pars_proxy',
            field=models.CharField(default=b'', max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
