from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """ Base Model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Folder(TimeStampedModel):
    """ Track Model """
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    parent_id = models.ForeignKey(
        'self',
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        related_name='child_folders'
        )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='folders'        
    )
    
    def __str__(self):
        return f'{self.name}'
