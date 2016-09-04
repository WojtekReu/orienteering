from django.db import models

from cms.models import CMSPlugin
from cup.models import Organizer, Marathon, Season, Route


class CupPlugin(CMSPlugin):
    organizer = models.ForeignKey(Organizer, verbose_name='Organizer name')
    marathon = models.ForeignKey(Marathon, verbose_name='Marathon')
    name = models.CharField(verbose_name='Adnotation', max_length=255)

    def __str__(self):
        return self.organizer.__str__()


class CupCalendar(CMSPlugin):
    season = models.ForeignKey(Season, verbose_name='Season of Marathon')

    def __str__(self):
        return self.season.__str__()


class CupOrganizer(CMSPlugin):
#    organizer = models.ForeignKey(Organizer, verbose_name='Organizer name')

    def __str__(self):
        return self.organizer.__str__()


class CupMarathon(CMSPlugin):

    def __str__(self):
        return self.marathon.__str__()


class CupRunner(CMSPlugin):

    def __str__(self):
        return self.runner.__str__()
