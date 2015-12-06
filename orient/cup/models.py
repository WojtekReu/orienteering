from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class BaseCup(models.Model):
    pass


class Organizer(BaseCup):
    user = models.ForeignKey(User)
    web = models.CharField(max_length=128)
    email = models.EmailField()
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
    organizer = models.ForeignKey(Organizer)
    season = models.ForeignKey(Season)
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
        return self.name


R_TYPE = {
    (0, 'TP50'),
    (1, 'TP100'),
    (2, 'TE150'),
    (3, 'TR100'),
    (4, 'TR200')
}


class Route(BaseCup):
    marathon = models.ForeignKey(Marathon)
    r_type = models.PositiveSmallIntegerField(choices=R_TYPE)
    start_time = models.DateTimeField()
    limit_time = models.PositiveSmallIntegerField()
    pk_points = models.PositiveSmallIntegerField()
    importance = models.PositiveSmallIntegerField(default=None, null=True) # range (0 - 105)

    def __str__(self):
        r_type_unicode = ''
        for row in R_TYPE:
            if row[0] == self.r_type:
                r_type_unicode = ' ' + row[1]
        return self.marathon.__str__() + r_type_unicode

GENDER = (
    (0, 'Male'),
    (1, 'Female')
)


class Runner(BaseCup):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    birth_date = models.DateField()
    locality = models.CharField(max_length=60)
    gender = models.BooleanField(default=None, choices=GENDER)    # True = Female, False = Male
    blog_url = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.user.__str__()

    def get_actual_category(self):
        #TODO: in progress
        return 'M, MW, K, KW'


class Result(BaseCup):
    runner = models.ForeignKey(Runner)
    route = models.ForeignKey(Route)
    r_number = models.PositiveIntegerField(default=None)
    meta_time = models.TimeField()
    total_time = models.TextField()
    pk_points = models.PositiveSmallIntegerField()
    penalty_points = models.PositiveSmallIntegerField()
    points = models.DecimalField(max_digits=6, decimal_places=2)

    def calc_category(self):
        #TODO: in progress
        return 'M, MW, k, KW'


class Forum(BaseCup):
    nick = models.CharField(max_length=80)
    # TODO: in progress, change this

