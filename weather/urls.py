from django.contrib import admin
from django.urls import path, include # import include to include urls in directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')),
]
