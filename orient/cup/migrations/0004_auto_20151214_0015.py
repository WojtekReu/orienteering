# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cup', '0003_auto_20151208_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='route',
            name='r_type',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='name',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='surname',
        ),
        migrations.AddField(
            model_name='result',
            name='ranking',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='category',
            field=models.TextField(default='', choices=[('TP50', 'Trasa Piesza 50 km'), ('TP100', 'Trasa Piesza 100 km'), ('TR100', 'Trasa Rowerowa 100 km'), ('TR200', 'Trasa Rowerowa 200 km')], max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marathon',
            name='organizer',
            field=models.ForeignKey(related_query_name='marathon', related_name='marathons', to='cup.Organizer'),
        ),
        migrations.AlterField(
            model_name='marathon',
            name='season',
            field=models.ForeignKey(related_query_name='marathon', related_name='marathons', to='cup.Season'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(related_query_name='organizer', related_name='organizers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='result',
            name='route',
            field=models.ForeignKey(related_query_name='result', related_name='results', to='cup.Route'),
        ),
        migrations.AlterField(
            model_name='result',
            name='runner',
            field=models.ForeignKey(related_query_name='result', related_name='results', to='cup.Runner'),
        ),
        migrations.AlterField(
            model_name='route',
            name='marathon',
            field=models.ForeignKey(related_query_name='route', related_name='routes', to='cup.Marathon'),
        ),
        migrations.AlterField(
            model_name='runner',
            name='gender',
            field=models.BooleanField(choices=[(0, 'Female'), (1, 'Male')]),
        ),
        migrations.AlterField(
            model_name='runner',
            name='user',
            field=models.ForeignKey(related_query_name='runner', related_name='runners', to=settings.AUTH_USER_MODEL),
        ),
    ]
