from django.conf.urls import url, patterns

from .views import IndexView, OrganizerView, OrganizerUpdateView, OrganizerCreateView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^or/(?P<pk>\d+)$', OrganizerView.as_view(), name='organizer'),
    url(r'^or-u/(?P<pk>\d+)$', OrganizerUpdateView.as_view(), name='organizer_update'),
    url(r'^or-c', OrganizerCreateView.as_view(), name='organizer_create'),
)
