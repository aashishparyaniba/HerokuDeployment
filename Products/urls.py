from django.urls import path

from Products import views

urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("women/", views.WomenProductPage.as_view(), name="womensProductPage"),
    path("women/<int:id>", views.ProductsDetailPage.as_view(), name="productDetailPage"),
    path("checkout/", views.CheckoutPage.as_view(), name="checkoutPage"),
]