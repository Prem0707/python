from django.shortcuts import render
from . import models
from django.db.models import Q
from django.core.urlresolvers import resolve

def perm_check(request, *args, **kwargs):
    url_name = resolve(request.path_info).url_name
    if url_name:
        # 获取请求方法，和请求参数
        url_method, url_args = request.method, request.GET
        url_args_list = []
        # 将各个参数的值用逗号隔开组成字符串，因为数据库中是这样存的
        for i in url_args:
            url_args_list.append(str(url_args[i]))
        url_args_list = ','.join(url_args_list)

        # get_perm = models.Permission.objects.filter(Q(url=url_name) and Q(per_method=url_method) and Q(argument_list=url_args_list))
        # if get_perm:
        perm_dic = {
            'views_student_list': ['student_list', 'GET', []],  # 权限字段名称(models表中定义)，URL别名,GET方法,请求参数
            'views_student_info': ['student_detail', 'GET', []],
        }
        for i in perm_dic:
            perm_name = 'students.{}'.format(i)
            if request.user.has_perm(perm_name):
                print('====》权限已匹配')
                return True
        # else:
        #     return False
        return False
    else:
        return False  # 没有权限设置，默认不放过

def check_permission(fun):
    def wapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):
            return fun(request, *args, **kwargs)
        return render(request, '403.html', locals())
    return wapper