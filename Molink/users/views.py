from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout


from . import serializers
from .models import User


class UserSignUp(APIView):

	# 회원가입
	def post(self, request, format=None):
		username = request.POST.get("username", 'username_error')
		password1 = request.POST.get("password1", 'password_error1')
		password2 = request.POST.get("password2", 'password_error2')
		if password1 != password2:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		elif password1 == password2:
			serializer = serializers.UserSignUpSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save(password=password1)
				user = User.objects.get(username=username, password=password1)
				if user:
					django_login(request, user)
					print("로그인됨")
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


class UserLogin(APIView):
	# 유저 로그인
	def get(self, request, format=None):
		username = request.POST.get("username", 'username_error')
		password = request.POST.get("password", 'password_error2')
		user = User.objects.get(username=username, password=password)
		if user:
			django_login(request, user)
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogout(APIView):
	# 유저 로그아웃
	def get(self, request, format=None):
		django_logout(request)
		return Response(status=status.HTTP_200_OK)

