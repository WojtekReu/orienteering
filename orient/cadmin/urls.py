# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf.urls import patterns

from .views import LoadRunnersFormView, LoadResultsFormView, MarathonResults

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(
        r'^admin/load-runners/$',
        LoadRunnersFormView.as_view(),
        name='load_runners'
    ),
    url(
        r'^admin/load-results/$',
        LoadResultsFormView.as_view(),
        name='load_results'
    ),
    url(
        r'^admin/get-runners/(?P<marathon_pk>\d+)/$',
        MarathonResults.as_view(),
        name='get_runners'
    ),
)
