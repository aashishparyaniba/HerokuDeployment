from django import forms

from Blogging.models import PublishBlog

class PublishBlogForm(forms.ModelForm):
    class Meta:
        model = PublishBlog
        fields = "__all__"
