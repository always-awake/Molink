from django.contrib import admin
from . import models

@admin.register(models.Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'parent_folder',
        'creator',
    )
