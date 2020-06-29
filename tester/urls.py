# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/6/21  14:50 
# 文件  urls
from django.urls import path
from tester import views

urlpatterns = [
    path('report/', views.report),
    path('case/',views.case),
    path('inter/',views.interface),

]