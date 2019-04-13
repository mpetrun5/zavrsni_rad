from django.contrib import admin

from agency.models import Agency


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass
