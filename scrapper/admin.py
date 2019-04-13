from django.contrib import admin

from scrapper.models import Selector


@admin.register(Selector)
class ScrapperAdmin(admin.ModelAdmin):
    pass
