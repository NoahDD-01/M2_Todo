from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexview , name = 'home'), 
]
