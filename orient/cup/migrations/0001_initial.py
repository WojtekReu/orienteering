# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('nick', models.CharField(max_length=80)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Marathon',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('locality', models.CharField(max_length=60)),
                ('logo_img', models.CharField(max_length=255)),
                ('web', models.CharField(max_length=128)),
                ('desc', models.TextField(default=None, null=True)),
                ('headquarter_address', models.CharField(max_length=255, default=None, null=True)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('web', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('desc', models.TextField(default=None, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('r_number', models.PositiveIntegerField(default=None)),
                ('meta_time', models.TimeField()),
                ('total_time', models.TextField()),
                ('pk_points', models.PositiveSmallIntegerField()),
                ('penalty_points', models.PositiveSmallIntegerField()),
                ('points', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('r_type', models.PositiveSmallIntegerField(choices=[(1, 'TP100'), (3, 'TR100'), (2, 'TE150'), (0, 'TP50'), (4, 'TR200')])),
                ('start_time', models.DateTimeField()),
                ('limit_time', models.PositiveSmallIntegerField()),
                ('pk_points', models.PositiveSmallIntegerField()),
                ('importance', models.PositiveSmallIntegerField(default=None, null=True)),
                ('marathon', models.ForeignKey(to='cup.Marathon')),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
                ('locality', models.CharField(max_length=60)),
                ('gender', models.BooleanField(default=None, choices=[(0, 'Male'), (1, 'Female')])),
                ('blog_url', models.CharField(max_length=255, default=None, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('basecup_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cup.BaseCup', primary_key=True, auto_created=True)),
                ('year', models.PositiveIntegerField()),
            ],
            bases=('cup.basecup',),
        ),
        migrations.AddField(
            model_name='result',
            name='route',
            field=models.ForeignKey(to='cup.Route'),
        ),
        migrations.AddField(
            model_name='result',
            name='runner',
            field=models.ForeignKey(to='cup.Runner'),
        ),
        migrations.AddField(
            model_name='marathon',
            name='organizer',
            field=models.ForeignKey(to='cup.Organizer'),
        ),
        migrations.AddField(
            model_name='marathon',
            name='season',
            field=models.ForeignKey(to='cup.Season'),
        ),
    ]
