from django.urls import path
from . import views

app_name = 'folders'
urlpatterns = [
	path('', views.Folder.as_view()),
	path('<int:folder_id>', views.Folder.as_view()),
	path('all', views.FolderList.as_view()),
]