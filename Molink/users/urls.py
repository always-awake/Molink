from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
	path('signup', views.UserSignUp.as_view()),
	path('login', views.UserLogin.as_view()),
]