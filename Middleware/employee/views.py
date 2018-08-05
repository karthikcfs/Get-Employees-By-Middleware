from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from employee.models import emp
from django.contrib.auth.decorators import login_required
# Create your views here.

def emp_login(request):
    c={}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            message = "User credential is not found"
            return HttpResponse(message)
    return render(request, 'emplogin.html')

def emp_logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

@login_required(login_url='/login/')
def emp_dashboard(request):
    c={}
    c.update(csrf(request))
    group_name = request.group_name
    employee_details = emp.objects.filter(department=str(group_name))
    emp_list = []
    if employee_details:
        for employee in employee_details:
            employee_detail = {'name': employee.name,
                               'emp_id': employee.emp_id,
                               'department': employee.department}
            emp_list.append(employee_detail)
    return render(request, 'dashboard.html', {'username': str(request.user),
                                              'groupname': str(group_name),
                                              'emp_list': emp_list})
