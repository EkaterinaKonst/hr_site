from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

def index(request):
    common_list = CommonInfo.objects.all
    places_list = Places.objects.all
    department_list = Department.objects.all
    subdepartment_list = SubDepartment.objects.all
    empl_list = Employer.objects.all
    context = {'common_list':common_list, 'places_list' : places_list,
               'department_list' : department_list,
               'subdepartment_list' : subdepartment_list,
               'empl_list' : empl_list}


    return render(request, 'HrBase/base.html', context)


