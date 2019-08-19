from django.conf import settings
from django.db import models

from folders.models import Folder, TimeStampedModel

class Link(TimeStampedModel):
    """ Link Model """
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='links',
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='links',
    )

    def __str__(self):
        return f'{self.name}-{self.parent_folder.name}'


