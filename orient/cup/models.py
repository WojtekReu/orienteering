from datetime import timedelta, date

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.timezone import datetime


class BaseCup(models.Model):
    pass


class BaseUser(User):
    phone = models.CharField(max_length=15)


class Organizer(BaseUser):
    web = models.CharField(max_length=128)
    desc = models.TextField(default=None, null=True)

    class Meta:
        verbose_name = _('Organizer')
        verbose_name_plural = _('Organizers')

    def __str__(self):
        return 'Organizer {} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('cup:organizer', kwargs={'pk': self.pk})


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
    logo_img = models.ImageField()     # logo url or path
    web = models.URLField(default=None, null=True)
    desc = models.TextField(default=None, null=True)
    headquarter_address = models.CharField(max_length=255, default=None, null=True)
    # position - TODO: add position

    def is_past(self):
        """
        Check is it past event by checking finish date.
        :return: True if marathon is finished.
        :rtype: bool
        """
        if self.end_date < date.today():
            return True
        return False

    def __str__(self):
        return self.name.__str__()

    def get_export_url(self):
        """
        Get url for export results data
        :return: url for export results
        :rtype: str
        """
        return reverse('get_runners', kwargs={'marathon_pk': self.pk})


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


class Runner(BaseUser):
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )
    VETERAN_DAYS = 13 * 366 + 37 * 365
    birth_date = models.DateField(default=None, null=True)
    birth_year = models.SmallIntegerField(default=None, null=True)
    locality = models.CharField(max_length=60)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    blog_url = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return 'Runner: {} {}'.format(self.first_name, self.last_name)

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

