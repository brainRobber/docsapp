# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driverId', models.AutoField(serialize=False, primary_key=True)),
                ('DriverFirstName', models.CharField(max_length=200)),
                ('DriverLastName', models.CharField(max_length=200)),
            ],
        ),
    ]
