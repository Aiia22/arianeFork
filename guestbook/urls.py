from django.urls import path
from . import views

## Define URLs for the App
urlpatterns = [
    path('', views.homepage, name='homepage'),
]