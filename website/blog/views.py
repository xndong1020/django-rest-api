from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Blogpost
from comment.models import Comment
from .forms import BlogpostForm
from django.contrib.auth.mixins import LoginRequiredMixin


# class BlogpostView(TemplateView):
#     template_name = 'blog/index.html'
#
#     # def get(self, request, *args, **kwargs):
#     #     posts = Blogpost.objects.all()
#     #     # test = Blogpost.objects.get(pk=2)
#     #     # print(test.comment_set.get(blogpost_id=2).body)
#     #     # print(posts.get(comment__blogpost_id=2).body)
#     #
#     #     response = [
#     #         {'id': post.id, 'title': post.title, 'author': post.author, 'body': post.body} for post in posts
#     #     ]
#     #
#     #     return self.render_to_response({'posts': response})
#
#     def get_context_data(self, **kwargs):
#         posts = Blogpost.objects.all()
#         response = [
#             {'id': post.id, 'title': post.title, 'author': post.author, 'body': post.body} for post in posts
#         ]
#
#         return {'posts': response}


class BlogpostView(LoginRequiredMixin, ListView):
    # template_name = 'blog/index.html'
    # model = Blogpost

    def get_template_names(self):
        return 'blog/index.html'

    def get_queryset(self):
        return Blogpost.objects.all()


# class BlogpostDetailView(TemplateView):
#     template_name = 'blog/detail.html'
#
#     def get_context_data(self, **kwargs):
#         pk = self.kwargs.get('pk')
#         try:
#             post = Blogpost.objects.get(pk=pk)
#         except Blogpost.DoesNotExist:
#             raise Http404
#         else:
#             context = {
#                 'title': post.title,
#                 'author': post.author,
#                 'body': post.body,
#                 'comments': post.comment_set.filter(blogpost_id=post.id)
#             }
#             return context

class BlogpostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/detail.html'
    model = Blogpost

    def get_context_data(self, **kwargs):
        # print(self.request.method)
        # print(self.request.user)
        # print(self.request.user.is_authenticated)
        pk = self.kwargs.get('pk')
        try:
            post = Blogpost.objects.get(pk=pk)
        except Blogpost.DoesNotExist:
            raise Http404
        else:
            context = {
                'title': post.title,
                'author': post.author,
                'body': post.body,
                'comments': post.comment_set.filter(blogpost_id=post.id)
            }
            return context


# class BlogpostCreateView(LoginRequiredMixin, TemplateView):
#     template_name = 'blog/create.html'
#
#     def get(self, request):
#         form = BlogpostForm()
#         return self.render_to_response({'form': form})
#
#     def post(self, request):
#         form = BlogpostForm(data=request.POST)
#         if not form.is_valid():
#             return self.render_to_response({'errors': form.errors})
#
#         blogpost = form.save(commit=False)
#         blogpost.user = request.user
#         blogpost.save()
#         return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blogpost.id}))

class BlogpostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'
    model = Blogpost

    fields = ['title', 'author', 'body', 'published']

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user  # set user
        return super(BlogpostCreateView, self).form_valid(form)


# class BlogpostEditView(LoginRequiredMixin, TemplateView):
#     template_name = "blog/edit.html"
#
#     def get(self, request, pk):
#         # equivalent to executing Blogpost.objects.get(pk=pk)
#         blogpost = get_object_or_404(Blogpost, pk=pk)
#
#         if blogpost.user != request.user:
#             raise Http404
#
#         form = BlogpostForm(instance=blogpost)
#         return self.render_to_response({'form': form, 'pk': pk})
#
#     def post(self, request, pk):
#         blogpost = get_object_or_404(Blogpost, pk=pk)
#
#         if blogpost.user != request.user:
#             raise Http404
#
#         form = BlogpostForm(data=request.POST, instance=blogpost)
#         if not form.is_valid():
#             return self.render_to_response({'errors': form.errors})
#
#         blogpost = form.save()
#         return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blogpost.id}))

class BlogpostEditView(LoginRequiredMixin, UpdateView):
    template_name = "blog/edit.html"
    model = Blogpost

    fields = ['title', 'author', 'body', 'published']

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})
