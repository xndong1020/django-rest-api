from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogpostView.as_view(), name="blog"),
    path('<int:pk>', views.BlogpostDetailView.as_view(), name="blogDetail"),
]
