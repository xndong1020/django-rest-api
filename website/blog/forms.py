from django import forms
from .models import Blogpost


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'author', 'body', 'published']

