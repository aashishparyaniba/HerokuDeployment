from django.urls import path

from Signupin import views

urlpatterns = [

    path("signup", views.Signup.as_view(), name="signup"),
    path("signin", views.Signin.as_view(), name="signin"),
    path("logout", views.Logout.as_view(), name="logout"),
]