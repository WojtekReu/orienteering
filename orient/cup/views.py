from django.shortcuts import render
from django.views import generic

from .models import Organizer


class IndexView(generic.TemplateView):
    template_name = 'cup/index.html'


