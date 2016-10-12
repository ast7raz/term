# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0002_calculate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculate',
            name='date',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
