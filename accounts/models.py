from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=64),
    phone_number = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.first_name
