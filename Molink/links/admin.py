from django.contrib import admin
from . import models

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'parent_id',
        'creator',
    )
