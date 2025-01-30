from django.urls import path
from . import views
from search.views import Search, Upload

urlpatterns = [
    path('', Search.as_view(), name='search'),
    path('search/', Search.as_view(), name='search'),
    path('upload/', Upload.as_view(), name='upload'),
    path('list/', views.list, name='list'),
    path('documents/<int:id>/', views.view_doc, name='document'),
    path('documents/<int:id>/<slug:slug>/', views.view_doc, name='document'),
    path('current_user/set/<int:id>/', views.set_user, name='set_user'),
]
