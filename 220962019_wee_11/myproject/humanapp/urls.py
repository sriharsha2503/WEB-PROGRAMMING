from django.urls import path
from . import views

urlpatterns = [
    path('', views.human_list, name='human_list'),
    path('get_human/', views.get_human, name='get_human'),
    path('update_human/', views.update_human, name='update_human'),
    path('delete_human/', views.delete_human, name='delete_human'),
]

