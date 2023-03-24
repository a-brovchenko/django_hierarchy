from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from django.db.models import Q
from django.shortcuts import render, redirect
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


def logout_view(request):
    logout(request)
    return redirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

    else:
        form = UserCreationForm()
    return render(request, 'employees/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'employees/profile.html', context)