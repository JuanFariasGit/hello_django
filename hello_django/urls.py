"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('hello/<nome>/<int:idade>/', views.hello),
    path('soma/<int:num1>/<int:num2>/', views.soma),
    path('multiplicacao/<int:num1>/<int:num2>/', views.multiplicacao),
    path('divisao/<int:num1>/<int:num2>/', views.divisao),
    path('tabuada_multiplicacao/<int:num>/', views.tabuada_multiplicacao),
    path('numeros_primos/<int:num>/', views.numeros_primos),
    path('fizzbuzz/', views.fizzbuzz)
]
