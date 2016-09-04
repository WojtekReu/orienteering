# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cup_plugin', '0003_cuporganizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuporganizer',
            name='organizer',
        ),
    ]
