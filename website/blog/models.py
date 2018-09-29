from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=240)
    author = models.CharField(max_length=240, db_index=True)
    body = models.TextField()

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

