from django.contrib import admin

from destination.models import Destination, Review


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_filter = ('agency', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
