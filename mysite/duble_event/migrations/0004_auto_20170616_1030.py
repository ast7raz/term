# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('duble_event', '0003_auto_20170609_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='exceptions',
            name='coment',
            field=models.CharField(default=b'', max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exceptions',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
