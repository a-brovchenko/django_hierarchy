from django.contrib.auth.forms import UserCreationForm
from .form import EmployeeForm
from .models import Employee
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'employees/index.html')

def employee_tree(request):
    nodes = Employee.objects.all()
    return render(request, 'employees/employee.html', {'nodes': nodes})


def employee_list(request):
    employees = Employee.objects.all()

    # get value for sorting
    sort_by = request.GET.get('sort', 'name')

    # filter
    query = request.GET.get('q')
    if query:
        employees = employees.filter(
            Q(name__icontains=query) | Q(position__icontains=query) | Q(email__icontains=query))

    # sort
    if sort_by in ['name', 'position', 'email', 'employment_date']:
        employees = employees.order_by(sort_by)

    context = {
        'employees': employees,
        'sort_by': sort_by,
        'query': query,
    }
    return render(request, 'employees/employee_list.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'employees/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'employees/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/index/')




@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'employees/profile.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:list')
    else:
        form = EmployeeForm()

    context = {'form': form}
    return render(request, 'employees/create_employee.html', context)


@login_required
def delete_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employee = get_object_or_404(Employee, name=name)
        employee.delete()
        return redirect('employees:list')

    return render(request, 'employees/delete_employee.html')


@login_required
def update_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employee = get_object_or_404(Employee, name=name)

        employee.name = request.POST.get('new_name', employee.name)
        employee.position = request.POST.get('new_position', employee.position)
        employee.email = request.POST.get('new_email', employee.email)
        employee.employment_date = request.POST.get('new_employment_date', employee.employment_date)
        employee.save()

        return redirect('employees:list')

    return render(request, 'employees/update_employee.html')
