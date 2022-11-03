"""werhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app1.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulimlar/', bulimlar ),
    path('client-update/<int:c>/', client_update ),
    path('clients/', clients),
    path('home/', home),
    path('product-update/<int:a>/', product_update),
    path('products/', products),
    path('stats/', stats),
    path('stats-update/<int:d>/', stats_update),
    path('tahrirlash/', tahrirlash),
]
