from django.db import models
from django.conf import settings


class Blogpost(models.Model):
    title = models.CharField(max_length=240)
    # if user is deleted, then all his/her blog will be deleted
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, default=None)
    author = models.CharField(max_length=240, db_index=True)
    body = models.TextField()

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

