"""
URL configuration for Django project.

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
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('classobj/', views.classobj, name='classobj'),
    path('interfaces/', views.interfaces, name='interfaces'),
    path('datatypes/', views.datatypes, name='datatypes'),
    path('datastorage/', views.datastorage, name='datastorage'),
    path('classes/', views.classes, name='classes'),
    path('objects/', views.objects, name='objects'),
    path('visibility/', views.visibility, name='visibility'),
    path('constructors/', views.constructors, name='constructors'),
    path('arrays/', views.arrays, name='arrays'),
    path('program/', views.program, name='program'),
    path('forl/', views.forl, name='forl'),
    path('ife/', views.ife, name='ife'),
    path('inherritance/', views.inherritance, name='inherritance'),
    path('input/', views.input, name='input'),
    path('polymorphism/', views.polymorphism, name='polymorphism'),
    path('overloading', views.overloading, name='overloading'),
    path('abstraction', views.abstraction, name='abstraction'),
    path('exception', views.exception, name='exception'),
    path('exception2', views.exception2, name='exception2'),
    path('exception3', views.exception3, name='exception3'),
    path('immutability', views.immutability, name='immutability'),
    path('interning', views.interning, name='interning'),
    path('chaining', views.chaining, name='chaining'),
    path('binding', views.binding, name='binding'),
    path('clone', views.clone, name='clone'),
    path('generic', views.generic, name='generic'),
    path('casting', views.casting, name='casting'),
    path('inner', views.inner, name='inner'),
    path('serialize', views.serialize, name='serialize'),
    path('deserialize', views.deserialize, name='deserialize')


]
