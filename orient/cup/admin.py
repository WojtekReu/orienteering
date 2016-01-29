from django.contrib import admin

from .models import Organizer, Marathon, Result, Runner, Route, Season


class OrganizerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'web',
    ]


class MarathonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Marathon, MarathonAdmin)
admin.site.register(Result)
admin.site.register(Route)
admin.site.register(Runner)
admin.site.register(Season)