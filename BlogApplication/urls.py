from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from BlogApplication import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", include("Products.urls")),
    #path("publish", include("Blogging.urls")),
    path("", include("Blogging.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATICFILES_DIRS}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
