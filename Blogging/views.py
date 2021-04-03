from django.shortcuts import render

from django.views import View
from Blogging.forms import PublishBlogForm


class PublishBlogFormView(View):
    def get(self, request):

        context = {}
        form = PublishBlogForm()
        context["form"] = form
        return render(request, "publishBlogForm.html", context)

    def post(self, request):
        context = {}
        form = PublishBlogForm(request.POST or None)
        context["form"] = form

        if form.is_valid():
            form.save()
        
        return render(request, "publishBlogForm.html", context)

class ShowAllPosts(View):
    def get(self, request):
        return render(request, "blog1.html")