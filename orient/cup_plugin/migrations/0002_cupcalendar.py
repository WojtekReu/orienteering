# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cup', '0003_auto_20151208_0128'),
        ('cms', '0013_urlconfrevision'),
        ('cup_plugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupCalendar',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True, serialize=False)),
                ('season', models.ForeignKey(to='cup.Season', verbose_name='Season of Marathon')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
