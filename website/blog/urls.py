from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogpostView.as_view(), name="blog-list"),
    path('<int:pk>', views.BlogpostDetailView.as_view(), name="blog-detail"),
    path('create', views.BlogpostCreateView.as_view(), name="blog-create"),
    path('edit/<int:pk>', views.BlogpostEditView.as_view(), name="blog-edit"),
]
