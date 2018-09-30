from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='accounts-signup'),
    path('login', views.LoginView.as_view(), name='accounts-login'),
    path('logout', views.LogoutView.as_view(), name='accounts-logout'),
]
