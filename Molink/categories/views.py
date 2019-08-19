import random
from folders.models import Folder
from folders.serializers import FolderSerializer
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
		return color_list[random_index]

	def post(self, request, format=None):
		user = request.user
		category_name_list = request.data['category_name_list']
		category_name_list = category_name_list.split(',')

		created_folers = []
		for category_name in category_name_list:
			folder = Folder()
			folder.name = category_name
			folder.color = self.get_random_color()
			folder.creator = user
			folder.save()
			created_folers.append(folder)
		folders = Folder.objects.filter(creator=user)
		serializer = FolderSerializer(folders, many=True)
		return Response(data=serializer.data, status=status.HTTP_201_CREATED)
