from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    # Add any custom fields here
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username