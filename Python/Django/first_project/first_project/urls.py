"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('djA9.urls')),
    # path(r'', include('djA8.urls')),
    # path(r'', include('djA7.urls')),
    # path(r'', include('djA6.urls')),
    # path(r'', include('djA4.urls')),
    # path(r'', include('demo.urls')),
    # path(r'', include('first_app.urls')),

    path("admin/", admin.site.urls),
]
