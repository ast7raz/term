# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cash_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.IntegerField()),
                ('coment', models.CharField(max_length=100)),
                ('cash', models.ForeignKey(to='phonebook.Cash')),
                ('club', models.ForeignKey(to='phonebook.Club')),
                ('parner', models.ForeignKey(to='phonebook.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cashs',
            name='club',
        ),
        migrations.RemoveField(
            model_name='cashs',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='cashs',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Cashs',
        ),
        migrations.RemoveField(
            model_name='clubs',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='clubs',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Clubs',
        ),
        migrations.RemoveField(
            model_name='partners',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Partners',
        ),
        migrations.RemoveField(
            model_name='rolls',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Phones',
        ),
        migrations.DeleteModel(
            name='Rolls',
        ),
        migrations.AddField(
            model_name='phone',
            name='rol',
            field=models.ForeignKey(to='phonebook.Roll'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='partner',
            field=models.ForeignKey(to='phonebook.Partner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cash',
            name='club',
            field=models.ForeignKey(to='phonebook.Club'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cash',
            name='partner',
            field=models.ForeignKey(to='phonebook.Partner'),
            preserve_default=True,
        ),
    ]
