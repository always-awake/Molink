from rest_framework import serializers

from . import models


class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Link
		fields = (
			'id',
			'name',
			'url',
			'parent_id',
		)
