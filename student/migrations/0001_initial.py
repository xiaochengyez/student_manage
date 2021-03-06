# Generated by Django 3.0.7 on 2020-06-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50, unique=True, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50, verbose_name='姓名')),
                ('student_gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别')),
                ('student_class', models.CharField(max_length=10, verbose_name='班级')),
                ('student_phone', models.CharField(max_length=25, verbose_name='联系方式')),
                ('student_address', models.CharField(max_length=25, verbose_name='地址')),
                ('student_label', models.CharField(max_length=200, verbose_name='标签')),
            ],
            options={
                'verbose_name': '学生信息',
                'db_table': 'StudentInfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
    ]
