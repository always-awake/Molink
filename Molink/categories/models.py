from django.db import models
from folders.models import TimeStampedModel


class Category(TimeStampedModel):
	""" Category Model """
	name = models.CharField(max_length=50)
	img_url = models.CharField(max_length=255)
