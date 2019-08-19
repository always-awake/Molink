from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import models


class FolderList(APIView):
	def get(self, request, format=None):
		user = request.user
		folders = models.Folder.objects.filter(creator=user, parent__isnull=True)
		serializer = serializers.FolderSerializer(folders, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)


class Folder(APIView):
	def post(self, request, format=None):
		user = request.user
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