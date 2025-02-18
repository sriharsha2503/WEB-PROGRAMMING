# magcover/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_cover, name='generate_cover'),
]

