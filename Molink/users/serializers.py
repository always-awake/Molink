from rest_framework import serializers

from . import models


class UserSignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = (
			'name', # 유저 이름
			'username', # 유저 아이디
			'password1', # 유저 패스워드 1
			'password2', # 유저 패스워드 2
		)
