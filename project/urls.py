# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/6/21  14:43 
# 文件  urls

from django.urls import path
from project import views

urlpatterns = [
    path('project/', views.project),
    path('add/', views.add_project),
    path('detail/', views.detail_project),
    path('', views.project),
    path('edit/', views.edit_project),



]