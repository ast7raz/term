# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reestrs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_reestr',
            name='request_level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
