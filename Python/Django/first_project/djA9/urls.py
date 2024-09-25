# Inside first_project/first_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index),
    path('adduserform', views.adduserform),
    path('adduser', views.adduser),
    path('showuser/<user_id>', views.showuser)
]