from django.urls import path
from . import views

app_name = 'folders'
urlpatterns = [
	path('', views.FolderList.as_view()),
]