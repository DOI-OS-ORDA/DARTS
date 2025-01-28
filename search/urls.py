from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
    path('list/', views.list, name='list'),
    path('documents/<int:id>/', views.view_doc, name='document'),
    path('documents/<int:id>/<slug:slug>/', views.view_doc, name='document'),
    path('current_user/set/<slug:type>', views.set_user, name='set_user'),
]
