from django.urls import path
from . import views

app_name = 'links'
urlpatterns = [
	path('', views.Link.as_view()),
	path('<int:link_id>', views.Link.as_view()),
]