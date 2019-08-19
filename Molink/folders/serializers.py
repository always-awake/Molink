from rest_framework import serializers

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
			'name',
			'color',
			'is_private',
			'parent_id',
		)

