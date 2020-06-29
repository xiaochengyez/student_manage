# Generated by Django 3.0.7 on 2020-06-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese', models.CharField(max_length=50, unique=True, verbose_name='语文')),
                ('mathematics', models.CharField(max_length=50, unique=True, verbose_name='数学')),
                ('English', models.CharField(max_length=50, unique=True, verbose_name='英语')),
                ('Chemistry', models.CharField(max_length=50, unique=True, verbose_name='化学')),
            ],
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('task_name', models.CharField(max_length=50, unique=True, verbose_name='任务名称')),
            ],
        ),
    ]
