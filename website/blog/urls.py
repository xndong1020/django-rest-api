from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogpostView.as_view(), name="blog-list"),
    path('<int:pk>', views.BlogpostDetailView.as_view(), name="blogDetail"),
    path('create', views.BlogpostCreateView.as_view(), name="blogCreate"),
    path('edit/<int:pk>', views.BlogpostEditView.as_view(), name="blogEdit"),
]
