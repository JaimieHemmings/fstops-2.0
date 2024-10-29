from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "quote"]


admin.site.register(Service, ServiceAdmin)