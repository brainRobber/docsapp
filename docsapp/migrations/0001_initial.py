# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('RequestID', models.AutoField(serialize=False, primary_key=True)),
                ('CustomerID', models.IntegerField()),
                ('RequestTime', models.DateTimeField(auto_now_add=True)),
                ('AcceptTime', models.DateTimeField()),
                ('isWaiting', models.BooleanField()),
                ('DriverId', models.IntegerField()),
            ],
        ),
    ]
