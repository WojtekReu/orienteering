# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cup', '0004_auto_20151214_0015'),
        ('cup_plugin', '0002_cupcalendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupOrganizer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True, serialize=False)),
                ('organizer', models.ForeignKey(verbose_name='Organizer name', to='cup.Organizer')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
