from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("home.urls")),
    path("news/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('services/', include('services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
