"""nested_serializers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path

# for our code 
from django.conf.urls import url
from django.urls.conf import include
from .core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'add/', views.BookView.as_view(), name='post'),
    path(r'addstate/', views.StateView.as_view(), name='poststate'),
    path(r'addtown/', views.TownView.as_view(), name='posttown'),
    url(r'upload/$', views.MyPhotoView.as_view(), name='file-upload'),
    path(r'entry/', views.One2ManyView.as_view(),name="One2Many"),
    path(r'person/', views.PersonView.as_view(),name="Person"),

]
