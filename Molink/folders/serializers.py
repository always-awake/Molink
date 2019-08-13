from rest_framework import serializers

from . import models


class FolderSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Folder
		fields = (
			'id',
			'color',
			'name',
			'created_at',
		)


class FolderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Folder
		fields = (
			'name',
			'color',
			'parent_id',
			'is_private',
		)

