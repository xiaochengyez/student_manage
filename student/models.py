from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    student_name = models.CharField('姓名',max_length=50,null=False)
    student_gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    student_class = models.CharField('班级',max_length=10,null=False)
    student_phone = models.CharField('联系方式',max_length=25,null=False)
    student_address = models.CharField('地址',max_length=25,null=False)
    student_label = models.CharField('标签',max_length=200,null=False)

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name = '学生信息'
        db_table = 'StudentInfo'


class ClassInfo(models.Model):
    class_name = models.CharField('班级名称',max_length=50,unique=True,null=False)


class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=20,unique=True,null=False)
    password = models.CharField('密码',max_length=20,null=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

class TaskInfo(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    task_name = models.CharField('任务名称', max_length=50, unique=True, null=False)

class MarkInfo(models.Model):
    chinese = models.CharField('语文', max_length=50, unique=True, null=False)
    mathematics = models.CharField('数学', max_length=50, unique=True, null=False)
    English = models.CharField('英语', max_length=50, unique=True, null=False)
    Chemistry = models.CharField('化学', max_length=50, unique=True, null=False)
