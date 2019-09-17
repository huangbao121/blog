"""blog URL Configuration

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
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('about/', views.about),
    path('index/', views.index),
    path('listpic/', views.listpic),
    path('newslistpic/', views.newslistpic),
    re_path('newslistpic/(\d+)', views.newslistpic),
    path('base/', views.base),
    path('add_article/', views.add_article),
    re_path('article_detail/(?P<id>\d+)', views.article_detail),
    path('fy_test/', views.fy_test),
    path('get_test/', views.get_test),
    path('form_test/', views.form_test),
    path('register/', views.register),
    path('blog/', include('appBlog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('enter/',views.enter)
]
