from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from . import serializers
from . import models
from folders.models import Folder


class Link(APIView):
	def post(self, request, format=None):
		user = request.user
		parent_folder = get_object_or_404(Folder, id=request.data['parent_id'], creator=user)
		serializer = serializers.LinkSerializer(data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save(creator=user, parent=parent_folder)
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, link_id, format=None):
		user = request.user
		try:
			parent_folder = get_object_or_404(Folder, id=request.data['parent_id'], creator=user)
			found_link = get_object_or_404(models.Link, id=link_id, creator=user)
			serializer = serializers.LinkSerializer(
				found_link, data=request.data, partial=True
			)
			if serializer.is_valid():
				serializer.save(parent=parent_folder)
				return Response(data=serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except KeyError:
			found_link = get_object_or_404(models.Link, id=link_id, creator=user)
			serializer = serializers.LinkSerializer(
				found_link, data=request.data, partial=True
			)
			if serializer.is_valid():
				serializer.save()
				return Response(data=serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

