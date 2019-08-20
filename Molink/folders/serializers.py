from rest_framework import serializers

from links.serializers import LinkSerializer
from . import models


class FolderSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Folder
		fields = (
			'id',
			'parent',
			'color',
			'name',
			'is_private',
			'created_at',
		)


class FolderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Folder
		fields = (
			'id',
			'name',
			'color',
			'parent_id',
			'is_private',
		)


class FolderGetSerializer(serializers.Serializer):
	folder = FolderSerializer()
	children_links = LinkSerializer(many=True)
	children_folders = FolderSerializer(many=True)
	sibling_folders = FolderSerializer(many=True)


