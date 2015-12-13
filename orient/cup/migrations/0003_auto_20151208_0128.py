# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cup', '0002_auto_20151206_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='r_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'TP50'), (1, 'TP100'), (2, 'TE150'), (3, 'TR100'), (4, 'TR200')]),
        ),
    ]
