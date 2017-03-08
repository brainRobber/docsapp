# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='DriverFirstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='DriverLastName',
            new_name='last_name',
        ),
    ]
