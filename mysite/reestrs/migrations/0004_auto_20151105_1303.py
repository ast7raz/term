# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reestrs', '0003_auto_20151105_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_reestr',
            old_name='cashsname',
            new_name='cashname',
        ),
        migrations.RenameField(
            model_name='request_reestr',
            old_name='intrument',
            new_name='instrument',
        ),
    ]
