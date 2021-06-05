from django.urls import path

from Blogging import views

urlpatterns = [
    path("publish/", views.PublishBlogFormView.as_view(), name="form"),
    path("", views.ShowAllPosts.as_view(), name="allBlogs"),
]