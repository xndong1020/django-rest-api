from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Blogpost
from comment.models import Comment
from .forms import BlogpostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogpostView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        posts = Blogpost.objects.all()
        # test = Blogpost.objects.get(pk=2)
        # print(test.comment_set.get(blogpost_id=2).body)
        # print(posts.get(comment__blogpost_id=2).body)

        response = [
            {'id': post.id, 'title': post.title, 'author': post.author, 'body': post.body} for post in posts
        ]

        return self.render_to_response({'posts': response})


class BlogpostDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/detail.html'

    def get(self, request, pk=None, *args, **kwargs):
        # aaa = self.kwargs.get('pk')
        # print(aaa)
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


class BlogpostCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/create.html'

    def get(self, request):
        form = BlogpostForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = BlogpostForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors': form.erros})

        blogpost = form.save(commit=False)
        blogpost.user = request.user
        blogpost.save()
        return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blogpost.id}))


class BlogpostEditView(LoginRequiredMixin, TemplateView):
    template_name = "blog/edit.html"

    def get(self, request, pk):
        # equivalent to executing Blogpost.objects.get(pk=pk)
        blogpost = get_object_or_404(Blogpost, pk=pk)

        if blogpost.user != request.user:
            raise Http404

        form = BlogpostForm(instance=blogpost)
        return self.render_to_response({'form': form, 'pk': pk})

    def post(self, request, pk):
        blogpost = get_object_or_404(Blogpost, pk=pk)

        if blogpost.user != request.user:
            raise Http404

        form = BlogpostForm(data=request.POST, instance=blogpost)
        if not form.is_valid():
            return self.render_to_response({'errors': form.erros})

        blogpost = form.save()
        return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blogpost.id}))

