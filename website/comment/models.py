from django.db import models
from django.conf import settings
from blog.models import Blogpost


class Comment(models.Model):
    body = models.CharField(max_length=500)
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
