from django.contrib import admin
from django.urls import path
from .models import Review, FAQ, AboutPage, Mosaic


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["name", "association"]
    list_display = ["name", "association", "review"]


class FAQAdmin(admin.ModelAdmin):
    search_fields = ["question"]
    list_display = ["question", "answer"]


class AboutPageAdmin(admin.ModelAdmin):
    search_fields = ["intro", "subtitle_one", "text_one", "body_one", "body_two", "body_three", "subtitle_two", "text_two", "body_four"]
    list_display = ["intro", "subtitle_one", "text_one", "body_one", "body_two", "body_image", "body_three", "subtitle_two", "text_two", "body_four"]


class MosaicAdmin(admin.ModelAdmin):
    search_fields = ["title", "description"]
    list_display = ["title"]
    

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(Mosaic, MosaicAdmin)
