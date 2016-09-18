# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupCalendar',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
                ('season', models.ForeignKey(verbose_name='Season of Marathon', to='cup.Season')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CupMarathon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CupOrganizer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CupPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
                ('name', models.CharField(max_length=255, verbose_name='Adnotation')),
                ('marathon', models.ForeignKey(verbose_name='Marathon', to='cup.Marathon')),
                ('organizer', models.ForeignKey(verbose_name='Organizer name', to='cup.Organizer')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CupRunner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
