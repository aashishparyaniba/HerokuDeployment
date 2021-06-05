from django.urls import path

from ShoppingCart import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path("cart", views.Cart.as_view(), name="cart"),
    path("orders", views.OrderView.as_view(), name="orders"),
    path("paymentsuccess", views.paymentSuccess.as_view(), name="paymentSuccess"),
]