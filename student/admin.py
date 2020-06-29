from django.contrib import admin

# Register your models here.
from student import models

admin.site.register(models.UserInfo)
admin.site.register(models.StudentInfo)
admin.site.register(models.ClassInfo)
