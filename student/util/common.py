# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/6/16  17:30 
# 文件  common
from student.models import StudentInfo


def delete_student(id):
    try:
        StudentInfo.objects.filter(id=id).delete()
        return 'ok'
    except Exception:
        return 'error'

def get_ajax_msg(msg, success):
    """
    ajax提示信息
    :param msg: str：msg
    :param success: str：
    :return:
    """
    return success if msg is 'ok' else msg
