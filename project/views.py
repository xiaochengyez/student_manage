from django.shortcuts import render

# Create your views here.
def add_project(request):
    return render(request,'project/project-add.html')


def detail_project(request):
    return render(request,'project/project-detail.html')


def edit_project(request):
    return render(request,'project/project-edit.html')


def project(request):
    return render(request,'project/projects.html')