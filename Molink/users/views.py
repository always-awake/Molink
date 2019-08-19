from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import models


class UserSignUp(APIView):

	# 회원가입
	def post(self, request, format=None):
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 != password2:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		elif password1 == password2:
			serializer = serializers.UserSignUpSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save(password=password1)
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfile(APIView):

	# 유저 정보 조회
	def get(self, request, format=None):
		pass
	# 유저 정보 수정
	def put(self, request, format=None):
		pass

class UserLoing(APIView):
	# 유저 로그인
	def post(self, request, format=None):
		pass


class UserLogout(APIView):
	# 유저 로그아웃
	def post(self, reqeust, format=None):
		pass
