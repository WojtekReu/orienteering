from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Organizer, Marathon, Result, Runner, Route, Season


class OrganizerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'web',
    ]


class MarathonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'export_url',
    ]
    readonly_fields = [
        'export_url',
    ]

    @staticmethod
    def export_url(instance):
        """
        Generate results export url
        :param instance: Marathon instance
        :return: html a tag
        :rtype: str
        """
        return mark_safe('<a href="{0}">export {1}</a>'.format(
            instance.get_export_url(),
            instance.name[:15]
        ))

admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Marathon, MarathonAdmin)
admin.site.register(Result)
admin.site.register(Route)
admin.site.register(Runner)
admin.site.register(Season)