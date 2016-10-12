# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0003_auto_20150219_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('admin', models.CharField(max_length=40, blank=True)),
                ('pas', models.CharField(max_length=40, blank=True)),
                ('ip', models.IPAddressField(blank=True)),
                ('version', models.CharField(max_length=40, blank=True)),
                ('club', models.ForeignKey(to='phonebook.Club')),
                ('part', models.ForeignKey(to='phonebook.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
