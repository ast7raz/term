# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duble_event', '0005_audio_file_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_file',
            name='file_path',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image_file',
            name='file_path',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
