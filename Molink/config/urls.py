from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/api/v1/admin/', admin.site.urls),
    path('/api/v1/folders/', include('folders.urls', namespace='folders')),
    path('/api/v1/links/', include('links.urls', namespace='links')),
    path('/api/v1/users/', include('users.urls', namespace='users')),
]
