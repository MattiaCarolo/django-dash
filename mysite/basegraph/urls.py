from django.urls import path
from . import views

urlpatterns = [
    path('', views.heat, name='heat'),
]
