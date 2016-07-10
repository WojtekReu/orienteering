# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from cup.models import Marathon


class LoadRunnersForm(forms.Form):
    """Load file users form"""

    marathon = forms.ChoiceField(
        choices=[(m.pk, m.name) for m in Marathon.objects.all()],
        required=False,
    )

    users_file = forms.FileField(
        label=_("Load csv file with users"),
    )


class LoadResultsForm(forms.Form):
    """Load file results for users form"""

    marathon = forms.ChoiceField(
        choices=[(m.pk, m.name) for m in Marathon.objects.all()],
        required=False,
    )

    results_file = forms.FileField(
        label=_("Load csv file with results")
    )

    def save(self, commit=False):
        # Save the provided password in hashed format
        super(LoadResultsForm, self).save(commit=False)
        print('LOADS RESULTS print here; ')

    def is_valid(self):
        """
        Check is it appropriate csv format and structure
        :return:
        """
        return super(LoadResultsForm, self).is_valid()

