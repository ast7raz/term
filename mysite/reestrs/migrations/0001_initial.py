# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_auto_20150331_1327'),
        ('default', '0003_alter_email_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instrument', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request_Reestr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('partname', models.CharField(max_length=300, blank=True)),
                ('clubname', models.CharField(max_length=100, blank=True)),
                ('cashsname', models.CharField(max_length=20, blank=True)),
                ('coment', models.CharField(max_length=500)),
                ('duration', models.IntegerField()),
                ('otrs_ticket', models.CharField(max_length=20, blank=True)),
                ('jira_BUG', models.CharField(max_length=10, blank=True)),
                ('request_level', models.IntegerField()),
                ('cash', models.ForeignKey(to='phonebook.Cash', blank=True)),
                ('club', models.ForeignKey(to='phonebook.Club', blank=True)),
                ('intrument', models.ForeignKey(to='reestrs.Request_Instrument')),
                ('partner', models.ForeignKey(to='phonebook.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request_subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_type', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='request_reestr',
            name='request_subject',
            field=models.ForeignKey(to='reestrs.Request_subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request_reestr',
            name='request_type',
            field=models.ForeignKey(to='reestrs.Request_type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request_reestr',
            name='user',
            field=models.ForeignKey(to='default.UserSocialAuth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request_reestr',
            name='user_position',
            field=models.ForeignKey(to='phonebook.Roll'),
            preserve_default=True,
        ),
    ]
