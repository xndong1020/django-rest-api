from django.urls import path
from .views import get_all_comments, get_comment_by_id_with_serializer

urlpatterns = [
    path('', get_all_comments, name="comment-list"),
    path('<int:pk>', get_comment_by_id_with_serializer, name="comment-detail"),
]
