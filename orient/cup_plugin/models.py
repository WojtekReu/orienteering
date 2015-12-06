from django.db import models

from cms.models import CMSPlugin
from cup.models import Organizer, Marathon


class CupPlugin(CMSPlugin):
    organizer = models.ForeignKey(Organizer, verbose_name='Organizer name')
    marathon = models.ForeignKey(Marathon, verbose_name='Marathon')
    name = models.CharField(verbose_name='Adnotation', max_length=255)

    def __str__(self):
        return self.organizer.__str__()
