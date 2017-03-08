# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsapp', '0002_auto_20170308_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='DriverId',
            new_name='DriverID',
        ),
    ]
