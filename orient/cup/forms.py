from django import forms

from .models import Organizer, Season, Runner, Marathon


class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['first_name', 'last_name', 'email', 'web', 'username', 'password', 'phone', 'desc']


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['year']


class MarathonForm(forms.ModelForm):
    class Meta:
        model = Marathon
        exclude = ()

