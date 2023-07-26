from django.http import HttpResponse
from django.shortcuts import redirect, render
from login.forms import EmployeeForm
from login.models import Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('main_screen')
        else:
            messages.info(request, 'Invalid username or password!')
            return redirect('login')
        

def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return render(request, 'logout.html')


login_required(login_url='login')
def main_screen(request):
    if request.user.is_authenticated:
        return render(request, 'main_screen.html')
    

def employees(request):
    if request.user.is_authenticated:
        employee = Employee.objects.all()

        context = {
            'employee': employee
        }

        return render(request, 'employees.html', context)

def employee_add(request):
    form = EmployeeForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main_screen')

    context = {
        'form':  form
    }

    return render (request, 'employee_add.html', context)


def employee_edit(request):
    
    employee = Employee.objects.all()

    context = {
        'employee': employee
    }

    employee_pk = request.GET.get('employee_pk')
    print(type(employee_pk))

    for emp in employee:
       emp.pk = str(emp.pk)
       if emp.pk == employee_pk:
            employee.id = employee_pk
            print('OK')
       
    
    return render(request, 'employee_edit.html', context)

def employee_update(request, employee_pk):

    employee = Employee.objects.get(pk=employee_pk)
    
    form = EmployeeForm(request.POST or None, instance=employee)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main_screen')

    context = {
        'form': form
    }

    return render (request, 'employee_update.html', context)


def employee_del(request):
    
    employee = Employee.objects.all()

    context = {
        'employee': employee
    }
  
    employee_pk = request.GET.get('employee_pk')
    print(type(employee_pk))

    for emp in employee:
       emp.pk = str(emp.pk)
       if emp.pk == employee_pk:
            employee.id = employee_pk
         
    return render(request, 'employee_del.html', context)


def employee_delete(request, employee_pk):
    employee = Employee.objects.get(pk=employee_pk)
    
    form = EmployeeForm(request.POST or None, instance=employee)

    if request.POST:
        if form.is_valid():
            employee.delete()
            return redirect('main_screen')

    context = {
        'form': form
    }

    return render (request, 'employee_delete.html', context)