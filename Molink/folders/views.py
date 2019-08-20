from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from . import serializers
from . import models
from links.models import Link


class FolderList(APIView):
	def get(self, request, format=None):
		user = request.user
		folders = models.Folder.objects.filter(creator=user, parent__isnull=True)
		serializer = serializers.FolderSerializer(folders, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)


class Folder(APIView):
	def post(self, request, format=None):
		user = request.user
		if request.data['parent_id'] is None:
			serializer = serializers.FolderCreateSerializer(data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save(creator=user)
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			try:
				parent_folder = models.Folder.objects.get(id=request.data['parent_id'], creator=user)
			except models.Folder.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)

			serializer = serializers.FolderCreateSerializer(data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save(creator=user, parent=parent_folder)
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, folder_id, format=None):
		user = request.user
		found_folder = get_object_or_404(models.Folder, id=folder_id, creator=user)
		children_folders = models.Folder.objects.filter(parent=found_folder, creator=user)
		children_links = Link.objects.filter(parent=found_folder, creator=user)

		if found_folder.parent is None:
			sibling_folders = models.Folder.objects.filter(parent__isnull=True, creator=user).exclude(id=folder_id)
		else:
			sibling_folders = models.Folder.objects.filter(parent=found_folder.parent, creator=user).exclude(id=folder_id)
		serializer_data = {
				"folder": found_folder,
				"children_folders": children_folders,
			    "children_links": children_links,
				"sibling_folders": sibling_folders
			 }
		results = serializers.FolderGetSerializer(serializer_data)
		return Response(data=results.data, status=status.HTTP_200_OK)

