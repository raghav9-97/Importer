"""Importer URL Configuration

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
from django.urls import path, re_path
from Products import views as prodview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addProducts/', prodview.addProducts, name='addingProd'),
    path('dashboard/', prodview.dashboard, name='Dashboard'),
    re_path(r'^products/(?P<stat>[-\w]+)/$', prodview.prodGrid, name="Gridview"),
    path('delProducts/', prodview.delProducts, name="deleteProd"),
    re_path(r'^(?P<identifier>[-\w]+)/$', prodview.deleteProd, name='delProd'),
]
