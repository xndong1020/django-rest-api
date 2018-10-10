from django.contrib import admin
from .models import ApplicationUser, ApplicationUserProfile

# Register your models here.
admin.site.register(ApplicationUser)
admin.site.register(ApplicationUserProfile)
