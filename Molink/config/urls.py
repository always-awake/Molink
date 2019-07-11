from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('folders/', include('folders.urls', namespace='folders')),
]
