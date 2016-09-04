# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('cup', '0004_auto_20151214_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='runner',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AlterModelManagers(
            name='organizer',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='runner',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='basecup_ptr',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='basecup_ptr',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='user',
        ),
        migrations.AlterField(
            model_name='marathon',
            name='web',
            field=models.CharField(max_length=128, default=None, null=True),
        ),
        migrations.AddField(
            model_name='organizer',
            name='baseuser_ptr',
            field=models.OneToOneField(auto_created=True, primary_key=True, default='', serialize=False, parent_link=True, to='cup.BaseUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runner',
            name='baseuser_ptr',
            field=models.OneToOneField(auto_created=True, primary_key=True, default='', serialize=False, parent_link=True, to='cup.BaseUser'),
            preserve_default=False,
        ),
    ]
