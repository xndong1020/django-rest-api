from django.views.generic import TemplateView
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import views
from django.urls import reverse
from .forms import UserSignupForm


class SignupView(TemplateView):
    template_name = 'user/signup.html'

    def get(self, request):
        form = UserSignupForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = UserSignupForm(data=request.POST)

        if not form.is_valid():
            return self.render_to_response({'errors': form.erros})

        user = form.save()
        return HttpResponseRedirect(reverse('blog-list'))


class LoginView(views.LoginView):
    template_name = 'user/login.html'


class LogoutView(views.LogoutView):
    template_name = 'user/login.html'
    next_page = '/accounts/login'


