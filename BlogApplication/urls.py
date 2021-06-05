from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from BlogApplication import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Products.urls")),
    path("", include("ShoppingCart.urls")),
    path("", include("Signupin.urls")),
    #path("", include("Blogging.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


