# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Symptom', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Found_duplicates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event1_id', models.CharField(max_length=15)),
                ('event2_id', models.CharField(max_length=15)),
                ('event1_date', models.DateTimeField()),
                ('event2_date', models.DateTimeField()),
                ('event1_name', models.CharField(max_length=100)),
                ('event2_name', models.CharField(max_length=100)),
                ('event1_sport', models.CharField(max_length=100)),
                ('event2_sport', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logging_duplicates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event1_id', models.CharField(max_length=15)),
                ('event2_id', models.CharField(max_length=15)),
                ('event1_date', models.DateTimeField()),
                ('event2_date', models.DateTimeField()),
                ('event1_name', models.CharField(max_length=100)),
                ('event2_name', models.CharField(max_length=100)),
                ('event1_sport', models.CharField(max_length=100)),
                ('event2_sport', models.CharField(max_length=100)),
                ('exception', models.BooleanField(default=False)),
                ('date_started_duble', models.DateTimeField(auto_now_add=True)),
                ('date_ended_duble', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parser_duble_event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100)),
                ('pars_url', models.URLField()),
                ('login', models.CharField(max_length=100, blank=True)),
                ('password', models.CharField(max_length=100, blank=True)),
                ('proxy_addr', models.CharField(max_length=100, blank=True)),
                ('proxy_port', models.CharField(max_length=5, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
