from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comment


def get_all_comments(request):
    queryset = Comment.objects.all()
    return JsonResponse(serializers.serialize('json', queryset), safe=False)


def get_comment_by_id(request, pk=None, *args, **kwargs):
    print(pk)
    [print(item) for item in kwargs]
    try:
        queryset = Comment.objects.filter(pk=pk)
    except Comment.DoesNotExist:
        raise Exception('The record you are looking for does not exist!')

    return HttpResponse(serializers.serialize('json', queryset))


@api_view(['GET'])  # api_view will set the .accepted_renderer before the response is returned from the view
def get_comment_by_id_with_serializer(request, pk=None, *args, **kwargs):
    try:
        queryset = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        raise Exception('The record you are looking for does not exist!')

    serializer = CommentSerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)
