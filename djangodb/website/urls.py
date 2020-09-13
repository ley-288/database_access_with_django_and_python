#step 4
from django.urls import path
from . import views #step 7

urlpatterns = [
    path('', views.home, name="home"), #step 6
    path('join', views.join, name="join"),
]
