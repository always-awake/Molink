import random
from folders.models import Folder
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Category


class CategoryList(APIView):
	def get(self, request, format=None):
		categories = Category.objects.all()
		serializer = serializers.CategorySerializer(categories, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryFolderCreate(APIView):

	def get_random_color(self):
		color_list = ["#39add1", "#3079ab", "#c25975", "#e15258",
		              "#f9845b", "#838cc7", "#7d669e", "#53bbb4",
		              "#51b46d", "#e0ab18", "#637a91", "#f092b0", "#b7c0c7"]
		random_index = random.randint(0, len(color_list) - 1)

		return color_list(random_index)

	def post(self, request, format=None):
		user = request.user

		category_name_list = request.POST['category_name']
		for category_name in category_name_list:
			folder = Folder()
			folder.name = category_name
			folder.color = self.get_random_color()


# class Folder(TimeStampedModel):
#     """ Track Model """
#     name = models.CharField(max_length=50)
#     color = models.CharField(max_length=20)
#     parent_folder = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name='child_folders'
#     )
#     creator = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         null=True,
#         related_name='folders'
#     )
#
#     def __str__(self):
#         return f'{self.name}'
