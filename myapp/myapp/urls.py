"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.views.generic import TemplateView, View
from app.views import index, index3, product_list, Index2, index4, hello, simple_post, add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('1/', simple_post),
    path('3/', index),
    path('index3/', index3),
    path('index/', Index2.as_view(template_name='index2.html')),
    path('index2/', product_list, name='index3'),
    path('index4/', add_product, name='add_product'),
]
