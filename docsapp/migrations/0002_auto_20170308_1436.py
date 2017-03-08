# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='isWaiting',
            new_name='isCompleted',
        ),
        migrations.AlterField(
            model_name='ride',
            name='AcceptTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
