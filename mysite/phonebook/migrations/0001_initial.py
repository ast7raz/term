# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cash_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.IntegerField()),
                ('coment', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rolls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_name', models.CharField(max_length=20)),
                ('phone', models.ForeignKey(to='phonebook.Phones')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='partners',
            name='phone',
            field=models.ManyToManyField(to='phonebook.Phones'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clubs',
            name='partner',
            field=models.ForeignKey(to='phonebook.Partners'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clubs',
            name='phone',
            field=models.ManyToManyField(to='phonebook.Phones'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cashs',
            name='club',
            field=models.ForeignKey(to='phonebook.Clubs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cashs',
            name='partner',
            field=models.ForeignKey(to='phonebook.Partners'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cashs',
            name='phone',
            field=models.ManyToManyField(to='phonebook.Phones'),
            preserve_default=True,
        ),
    ]
