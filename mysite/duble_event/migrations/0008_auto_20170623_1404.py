# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duble_event', '0007_user_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_config',
            name='image_file',
            field=models.ForeignKey(blank=True, to='duble_event.Image_file', null=True),
            preserve_default=True,
        ),
    ]
