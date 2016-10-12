# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0005_auto_20160928_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parser_users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40)),
                ('userpass', models.CharField(max_length=40)),
                ('parser', models.CharField(max_length=20)),
                ('parsurl', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
