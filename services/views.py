from django.shortcuts import render

def services(request):
    return render(request, "services/services.html")


def services_headshots(request):
    return render(request, "services/service-page.html")


def services_event(request):
    return render(request, "services/service-page.html")


def services_lifestyle(request):
    return render(request, "services/service-page.html")


def services_product(request):
    return render(request, "services/service-page.html")


def services_property(request):
    return render(request, "services/service-page.html")


def services_aerial(request):
    return render(request, "services/service-page.html")