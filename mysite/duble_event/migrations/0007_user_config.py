# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('duble_event', '0006_auto_20170621_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.IntegerField(default=1)),
                ('transparent', models.IntegerField(default=0)),
                ('hex_color', models.CharField(default=b'#ffffff', max_length=7)),
                ('audio_file', models.ForeignKey(to='duble_event.Audio_file')),
                ('image_file', models.ForeignKey(to='duble_event.Image_file', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
