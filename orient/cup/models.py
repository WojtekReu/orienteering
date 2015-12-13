from datetime import timedelta, date

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.timezone import datetime


class BaseCup(models.Model):
    pass


class Organizer(BaseCup):
    user = models.ForeignKey(User, related_name='organizers', related_query_name='organizer')
    web = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    desc = models.TextField(default=None, null=True)

    class Meta:
        verbose_name = _('Organizer')
        verbose_name_plural = _('Organizers')

    def __str__(self):
        return self.user.__str__()


class Season(BaseCup):
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.year.__str__()


class Marathon(BaseCup):
    organizer = models.ForeignKey(Organizer, related_name='marathons',
                                  related_query_name='marathon')
    season = models.ForeignKey(Season, related_name='marathons', related_query_name='marathon')
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    locality = models.CharField(max_length=60)
    logo_img = models.CharField(max_length=255)     # logo url or path
    web = models.CharField(max_length=128)
    desc = models.TextField(default=None, null=True)
    headquarter_address = models.CharField(max_length=255, default=None, null=True)
    # position - TODO: add position

    def __str__(self):
        return self.name.__str__()


class Route(BaseCup):
    CATEGORY_TP50 = 'TP50'
    CATEGORY_TP100 = 'TP100'
    CATEGORY_TR100 = 'TR100'
    CATEGORY_TR200 = 'TR200'
    CATEGORY_CHOICES = (
        (CATEGORY_TP50, "Trasa Piesza 50 km"),
        (CATEGORY_TP100, "Trasa Piesza 100 km"),
        (CATEGORY_TR100, "Trasa Rowerowa 100 km"),
        (CATEGORY_TR200, "Trasa Rowerowa 200 km"),
    )
    marathon = models.ForeignKey(Marathon, related_name='routes', related_query_name='route')
    category = models.TextField(max_length=5, choices=CATEGORY_CHOICES)
    start_time = models.DateTimeField()
    limit_time = models.PositiveSmallIntegerField()
    pk_points = models.PositiveSmallIntegerField()
    importance = models.PositiveSmallIntegerField(default=None, null=True) # range (0 - 105)

    def __str__(self):
        return "{} {}".format(self.marathon, self.category)


class Runner(BaseCup):
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )
    VETERAN_DAYS = 13 * 366 + 47 * 365
    user = models.ForeignKey(User, related_name='runners', related_query_name='runner')
    birth_date = models.DateField()
    locality = models.CharField(max_length=60)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    blog_url = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.user.__str__()

    def get_actual_category(self):
        if self.gender == self.GENDER_FEMALE:
            if date.today() - self.birth_date < timedelta(days=self.VETERAN_DAYS):
                # TODO: calculate more correctly: by year difference and compare month and day.
                return 'K'
            else:
                return 'KW'
        if self.gender == self.GENDER_MALE:
            if date.today() - self.birth_date < timedelta(days=self.VETERAN_DAYS):
                return 'M'
            else:
                return 'MW'


class Result(BaseCup):
    RANKING_K = 'K'
    RANKING_KW = 'KW'
    RANKING_M = 'M'
    RANKING_MW = 'MW'
    RANKING_CHOICES = (
        (RANKING_K, 'Women'),
        (RANKING_KW, 'Veteran Women'),
        (RANKING_M, 'Men'),
        (RANKING_MW, 'Veteran Men'),
    )
    runner = models.ForeignKey(Runner, related_name='results', related_query_name='result')
    route = models.ForeignKey(Route, related_name='results', related_query_name='result')
    r_number = models.PositiveIntegerField(default=None)
    meta_time = models.TimeField()
    total_time = models.TextField()
    pk_points = models.PositiveSmallIntegerField()
    penalty_points = models.PositiveSmallIntegerField()
    ranking = models.CharField(max_length=2)
    points = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} {}'.format(self.runner, self.total_time)


class Forum(BaseCup):
    nick = models.CharField(max_length=80)
    # TODO: in progress, change this

