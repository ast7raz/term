# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_auto_20150209_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='parner',
            new_name='partner',
        ),
    ]
