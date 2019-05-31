from django.contrib import admin

from destination.models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_filter = ('agency', )
