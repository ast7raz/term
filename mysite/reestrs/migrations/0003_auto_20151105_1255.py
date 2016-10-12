# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reestrs', '0002_auto_20151103_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_reestr',
            name='cash',
            field=models.ForeignKey(blank=True, to='phonebook.Cash', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request_reestr',
            name='club',
            field=models.ForeignKey(blank=True, to='phonebook.Club', null=True),
            preserve_default=True,
        ),
    ]
