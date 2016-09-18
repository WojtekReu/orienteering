# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('basecup_ptr', models.OneToOneField(to='cup.BaseCup', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=80)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Marathon',
            fields=[
                ('basecup_ptr', models.OneToOneField(to='cup.BaseCup', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('locality', models.CharField(max_length=60)),
                ('logo_img', models.ImageField(upload_to='')),
                ('web', models.URLField(default=None, null=True)),
                ('desc', models.TextField(default=None, null=True)),
                ('headquarter_address', models.CharField(default=None, max_length=255, null=True)),
                ('has_results', models.BooleanField(default=False)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('baseuser_ptr', models.OneToOneField(to='cup.BaseUser', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('web', models.CharField(max_length=128)),
                ('desc', models.TextField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
            bases=('cup.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('basecup_ptr', models.OneToOneField(to='cup.BaseCup', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('r_number', models.PositiveIntegerField(default=None)),
                ('meta_time', models.TimeField(default=None)),
                ('total_time', models.TextField(default=None)),
                ('pk_points', models.PositiveSmallIntegerField(default=None)),
                ('penalty_points', models.PositiveSmallIntegerField(default=None)),
                ('ranking', models.CharField(default=None, max_length=2)),
                ('points', models.DecimalField(default=None, max_digits=6, decimal_places=2)),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('basecup_ptr', models.OneToOneField(to='cup.BaseCup', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('category', models.TextField(choices=[('TP50', 'Trasa Piesza 50 km'), ('TP100', 'Trasa Piesza 100 km'), ('TR100', 'Trasa Rowerowa 100 km'), ('TR200', 'Trasa Rowerowa 200 km')], max_length=5)),
                ('start_time', models.DateTimeField()),
                ('limit_time', models.PositiveSmallIntegerField()),
                ('pk_points', models.PositiveSmallIntegerField()),
                ('importance', models.PositiveSmallIntegerField(default=None, null=True)),
                ('marathon', models.ForeignKey(related_query_name='route', related_name='routes', to='cup.Marathon')),
            ],
            bases=('cup.basecup',),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('baseuser_ptr', models.OneToOneField(to='cup.BaseUser', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('birth_date', models.DateField(default=None, null=True)),
                ('birth_year', models.SmallIntegerField(default=None, null=True)),
                ('locality', models.CharField(max_length=60)),
                ('gender', models.BooleanField(choices=[(0, 'Female'), (1, 'Male')])),
                ('blog_url', models.CharField(default=None, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('cup.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('basecup_ptr', models.OneToOneField(to='cup.BaseCup', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveIntegerField()),
            ],
            bases=('cup.basecup',),
        ),
        migrations.AddField(
            model_name='result',
            name='route',
            field=models.ForeignKey(related_query_name='result', related_name='results', to='cup.Route'),
        ),
        migrations.AddField(
            model_name='result',
            name='runner',
            field=models.ForeignKey(related_query_name='result', related_name='results', to='cup.Runner'),
        ),
        migrations.AddField(
            model_name='marathon',
            name='organizer',
            field=models.ForeignKey(related_query_name='marathon', related_name='marathons', to='cup.Organizer'),
        ),
        migrations.AddField(
            model_name='marathon',
            name='season',
            field=models.ForeignKey(related_query_name='marathon', related_name='marathons', to='cup.Season'),
        ),
    ]
