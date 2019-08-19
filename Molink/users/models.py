from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Model """
    # username = user_id
    # password = user_password
    name = models.CharField(max_length=155, null=True, blank=False)
    password1 = models.CharField(max_length=155, null=True, blank=False)
    password2 = models.CharField(max_length=155, null=True, blank=False)
