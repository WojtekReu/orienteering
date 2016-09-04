from django.conf.urls import url, patterns

from .views import IndexView, OrganizerView, OrganizerUpdateView, OrganizerCreateView,\
    MarathonDetailView, RunnerDetailView, latest_m

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^or/(?P<pk>\d+)$', OrganizerView.as_view(), name='organizer'),
    url(r'^or-u/(?P<pk>\d+)$', OrganizerUpdateView.as_view(), name='organizer_update'),
    url(r'^or-c', OrganizerCreateView.as_view(), name='organizer_create'),
    url(r'^marathon/(?P<pk>\d+)$', MarathonDetailView.as_view(), name='marathon_runners'),
    url(r'^runner/(?P<pk>\d+)$', RunnerDetailView.as_view(), name='runner'),
    url(r'^latestm$', latest_m, name='latest_m'),
)
