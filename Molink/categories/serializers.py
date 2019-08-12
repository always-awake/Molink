from rest_framework import serializers

from .models import Category
from folders.models import Folder


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'img_url',
            'name',
        )


