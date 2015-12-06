# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cup', '0002_auto_20151206_2028'),
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Adnotation')),
                ('marathon', models.ForeignKey(to='cup.Marathon', verbose_name='Marathon')),
                ('organizer', models.ForeignKey(to='cup.Organizer', verbose_name='Organizer name')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
