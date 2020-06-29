"""student_platform URL Configuration

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
from django.urls import path, include

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_student,),
    path('edit/<int:id>', views.edit_student),
    path('details/<int:id>', views.details),
    path('', views.login),
    path('index/', views.index),
    path('student_search/', views.student_search),
    path('login/', views.login),
    path('student/',views.student),
    path('project/', include('project.urls')),
    path('test/', include('tester.urls')),



    path('timeline',views.timeline),
    path('top/',views.message),
    path('calendar/',views.calendar),
    path('contact/',views.contact),
    path('profile/',views.profile),

]
