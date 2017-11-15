from django.shortcuts import render
from . import models
from .permission import  check_permission
# Create your views here.

@check_permission
def students(request):
    students_obj = models.Student.objects.all()
    return render(request, 'students/student_list.html', locals())