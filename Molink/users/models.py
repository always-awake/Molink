from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Model """

    phone_uuid = models.CharField(max_length=255)