
from django.contrib import admin
from django.urls import path, include #step 1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), #step 2
]
