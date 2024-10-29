from django.shortcuts import render
from home.models import Review
from .models import Service

def services(request):
    reviews = Review.objects.all()
    services = Service.objects.all()
    context = {
        'services': services,
        'reviews': reviews
    }
    return render(request, "services/services.html", context)


def service_details(request, title):
    service = Service.objects.get(name=title)
    context = {
        'service': service
    }
    return render(request, "services/service-page.html", context)