from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CupPlugin, CupCalendar, CupOrganizer

__author__ = 'orkan'


class CMSCupPlugin(CMSPluginBase):
    model = CupPlugin
    module = _("Cup")
    name = _("Cup Plugin")
    render_template = "djangocms_cup/cup_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSCupPlugin)


class CMSRegistrationPlugin(CMSPluginBase):
    module = _("Cup")
    name = _("Registration")
    render_template = "djangocms_cup/cup_registration.html"

plugin_pool.register_plugin(CMSRegistrationPlugin)


class CMSCalendarPlugin(CMSPluginBase):
    model = CupCalendar
    module = _("Cup")
    name = _("Calendar")
    render_template = "djangocms_cup/cup_calendar.html"

plugin_pool.register_plugin(CMSCalendarPlugin)


class CMSOrganizerPlugin(CMSPluginBase):
#    model = CupOrganizer
    module = _("Cup")
    name = _("Organizer")
    render_template = "djangocms_cup/cup_organizer.html"

plugin_pool.register_plugin(CMSOrganizerPlugin)
