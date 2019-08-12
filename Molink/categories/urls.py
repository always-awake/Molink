from django.urls import path
from . import views

app_name = 'categories'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='category_list'),
]