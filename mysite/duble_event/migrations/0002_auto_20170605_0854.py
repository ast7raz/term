# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duble_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logging_duplicates',
            name='date_ended_duble',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
