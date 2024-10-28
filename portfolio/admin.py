from django.contrib import admin
from .models import Portfolio
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Portfolio)
admin.site.register(Category)


