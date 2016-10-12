# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reestrs', '0004_auto_20151105_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='request_reestr',
            name='state',
            field=models.ForeignKey(default=1, to='reestrs.Request_state'),
            preserve_default=False,
        ),
    ]
