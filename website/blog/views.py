from django.http import HttpResponse, Http404
from django.views.generic import View
from blog.models import Blogpost


class BlogpostView(View):
    def get(self, request):
        posts = Blogpost.objects.all()

        response = [
            "{id}: {title} by {author}<br>".format(id=post.id, title=post.title, author=post.author) for post in posts
        ]

        return HttpResponse(response)


class BlogpostDetailView(View):
    def get(self, request, pk=None):
        try:
            post = Blogpost.objects.get(pk=pk)
        except Blogpost.DoesNotExist:
            raise Http404
        else:
            response = "{id}: {title} by {author}<br>".format(id=post.id, title=post.title, author=post.author)
            return HttpResponse(response)
