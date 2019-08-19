from django.urls import path
from . import views

app_name = 'categories'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='category_list'),
    path('folders', views.CategoryFolderCreate.as_view(), name='create_category_folder'),
]