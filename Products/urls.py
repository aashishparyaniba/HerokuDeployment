from django.urls import path

from Products import views

urlpatterns = [
    path("", views.Products.as_view()),
]