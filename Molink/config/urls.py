from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('folders/', include('folders.urls', namespace='folders')),
    path('links/', include('links.urls', namespace='links')),
    path('users/', include('users.urls', namespace='users')),
]
