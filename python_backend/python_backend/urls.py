from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api_v1/', include('backend.urls')),
    path('admin/', admin.site.urls),
]
