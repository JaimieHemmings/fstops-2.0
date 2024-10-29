from django.contrib import admin
from django.urls import path
from .models import Review, FAQ


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["name", "association"]
    list_display = ["name", "association", "review"]


class FAQAdmin(admin.ModelAdmin):
    search_fields = ["question"]
    list_display = ["question", "answer"]
    

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Review, ReviewAdmin)
