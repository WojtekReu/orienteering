# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='r_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'TP50'), (2, 'TE150'), (3, 'TR100'), (4, 'TR200'), (1, 'TP100')]),
        ),
    ]
