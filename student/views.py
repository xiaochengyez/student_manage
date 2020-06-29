import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from student.models import UserInfo, ClassInfo, StudentInfo, TaskInfo
from student.util.common import delete_student, get_ajax_msg


def login_check(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('login_status'):
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)
    return wrapper


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('passwd')
        if UserInfo.objects.filter(username__exact=username).filter(password__exact=password).count() == 1:
            request.session['login_status'] = True
            request.session['now_account'] = username
            return HttpResponseRedirect('/index/')
        else:
            request.session['login_status'] = False
            message = {'message':'账号或密码错误'}
            return render(request,'login.html',message)
    elif request.method == 'GET':
        return render(request,"login.html")

@login_check
def student(request):
    if request.is_ajax():
        kwargs = json.loads(request.body.decode('utf-8'))
        mode = kwargs.pop('mode')
        id = kwargs.pop('id')
        if mode == 'del':
            msg = delete_student(id)
        return HttpResponse(get_ajax_msg(msg, 'ok'))
    else:
        user = request.session['now_account']
        class_list = ClassInfo.objects.all()
        student_list = StudentInfo.objects.all()
        return render(request, 'student.html', {'user':user, 'student_list':student_list, 'class_list':class_list})

@login_check
def add_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name', '')
        student_gender = request.POST.get('student_gender', '')
        student_class = request.POST.get('student_class','')
        student_phone = request.POST.get('phone', '')
        student_address = request.POST.get('address', '')
        student_label = request.POST.get('label')
        student = StudentInfo(student_name=student_name,student_gender=student_gender,student_class=student_class,student_phone=student_phone,
                              student_address=student_address,student_label=student_label)
        student.save()
        return HttpResponseRedirect('/index/')
    elif request.method == 'GET':
        user = request.session["now_account"]
        class_list = ClassInfo.objects.all()
        return render(request,"add_student.html",{'user':user,'class_list':class_list})

@login_check
def edit_student(request,id):
    if request.method == 'POST':
        student_name = request.POST.get('student_name', '')
        student_gender = request.POST.get('student_gender', '')
        student_class = request.POST.get('student_class', '')
        student_phone = request.POST.get('phone', '')
        student_address = request.POST.get('address', '')
        student_label = request.POST.get('label')
        StudentInfo.objects.filter(id=id).update(student_name=student_name, student_gender=student_gender, student_class=student_class,
                              student_phone=student_phone,
                              student_address=student_address, student_label=student_label)
        return HttpResponseRedirect('/index/')
    elif request.method == 'GET':
        user = request.session["now_account"]
        student = get_object_or_404(StudentInfo, id=id)
        class_list = ClassInfo.objects.all()
        return render(request,"edit_student.html",{'student_name':student.student_name,
                                                   'student_gender': student.get_student_gender_display(),
                                                   'student_gender_display': student.get_student_gender_display(),
                                                   'student_class': class_list,
                                                   'phone': student.student_phone,
                                                   'address':student.student_address,
                                                   'label':student.student_label,
                                                   'id': student.id,
                                                   'user':user})
    return render(request,'edit_student.html')

@login_check
def details(request,id):
    user = request.session['now_account']
    student_list = StudentInfo.objects.filter(id=id)
    result =100
    label = student_list[0].student_name + ' :' + student_list[0].student_label
    return render(request,'details.html',{'student_list':student_list,'label':label,'user':user,'result':result})

@login_check
def logout(request):
    if request.method == 'GET':
        del request.session['now_account']
        del request.session['login_status']
        return render(request,'login.html')

@login_check
def student_search(request):
    user = request.session["now_account"]
    name = request.GET.get('student_name', '')
    if name is None or name != '':
        student_list = StudentInfo.objects.filter(student_name=name)
        class_list = ClassInfo.objects.all()
        return render(request, 'student.html', {'student_list': student_list, 'class_list':class_list,
                                              'user': user})
    else:
        student_list = StudentInfo.objects.all()
        class_list = ClassInfo.objects.all()
        return render(request, 'student.html', {'student_list': student_list, 'class_list': class_list,
                                              'user': user})

@login_check
def index(request):
    user = request.session['now_account']
    task_list = TaskInfo.objects.all()
    return render(request, 'index.html',{'user':user,'task_list':task_list})

@login_check
def timeline(request):
    return render(request,'timeline.html')

@login_check
def calendar(request):
    return render(request,'calendar.html')

@login_check
def contact(request):
    user = request.session['now_account']
    student_list = StudentInfo.objects.all()
    return render(request, 'contacts.html', {'user': user, 'student_list': student_list})

@login_check
def message(request):
    return render(request, 'message.html')

@login_check
def profile(request):
    return render(request,'profile.html')


