from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from . import serializers


class CategoryListAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)