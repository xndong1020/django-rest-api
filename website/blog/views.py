from django.http import Http404
from django.views.generic import TemplateView
from blog.models import Blogpost


class BlogpostView(TemplateView):
    template_name = 'blog/index.html'
    def get(self, request):
        posts = Blogpost.objects.all()

        response = [
            {'id': post.id, 'title': post.title, 'author': post.author, 'body': post.body} for post in posts
        ]

        return self.render_to_response({'posts': response})


class BlogpostDetailView(TemplateView):
    template_name = 'blog/detail.html'

    def get(self, request, pk=None):
        try:
            post = Blogpost.objects.get(pk=pk)
        except Blogpost.DoesNotExist:
            raise Http404
        else:
            context = {
                'title': post.title,
                'author': post.author,
                'body': post.body,
            }
            return self.render_to_response(context)
