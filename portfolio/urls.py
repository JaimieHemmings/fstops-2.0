from django.urls import path
from . import views

urlpatterns = [
  path("", views.portfolio, name="portfolio"),
  path("<slug:slug>/", views.portfolio_item, name="portfolio_item"),
]
