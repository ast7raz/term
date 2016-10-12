# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0003_auto_20150219_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partner',
            name='part_name',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phone',
            name='coment',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roll',
            name='roll_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
