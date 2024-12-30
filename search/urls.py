from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
    path('list/', views.list, name='list'),
]
