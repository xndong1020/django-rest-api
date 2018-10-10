from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class ApplicationUserProfile(models.Model):
    avatar = models.CharField(max_length=300, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# each user will have a profile associated with
class ApplicationUser(AbstractUser):
    pass


