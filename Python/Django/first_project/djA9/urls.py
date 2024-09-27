# Inside first_project/first_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index),
    path('adduserform', views.adduserform),
    path('adduser', views.adduser),
    path('showuser/<user_id>', views.showuser),
    path('edituser/<user_id>', views.edituser),
    path('deleteuser/<user_id>', views.deleteuser),
    path('edituserform/<user_id>', views.edituserform)
]