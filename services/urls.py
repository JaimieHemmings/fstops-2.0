from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("", views.services, name="services"),
  path("headshots/", views.services_headshots, name="services_headshots"),
  path("event/", views.services_event, name="services_event"),
  path("lifestyle/", views.services_lifestyle, name="services_lifestyle"),
  path("product/", views.services_product, name="services_product"),
  path("property/", views.services_property, name="services_property"),
  path("aerial/", views.services_aerial, name="services_aerial"),
]