from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Blogpost
from .forms import BlogpostForm


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


class BlogpostCreateView(TemplateView):
    template_name = 'blog/create.html'

    def get(self, request):
        form = BlogpostForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = BlogpostForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors': form.erros})

        blogpost = form.save()
        return HttpResponseRedirect(reverse('blogDetail', kwargs={'pk': blogpost.id}))


class BlogpostEditView(TemplateView):
    template_name = "blog/edit.html"

    def get(self, request, pk):
        # equivalent to executing Blogpost.objects.get(pk=pk)
        blogpost = get_object_or_404(Blogpost, pk=pk)
        form = BlogpostForm(instance=blogpost)
        return self.render_to_response({'form': form, 'pk': pk})

    def post(self, request, pk):
        blogpost = get_object_or_404(Blogpost, pk=pk)
        form = BlogpostForm(data=request.POST, instance=blogpost)
        if not form.is_valid():
            return self.render_to_response({'errors': form.erros})

        blogpost = form.save()
        return HttpResponseRedirect(reverse('blogDetail', kwargs={'pk': blogpost.id}))

