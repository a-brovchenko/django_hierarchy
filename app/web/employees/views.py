from django.shortcuts import render
from .models import Employee
from django.db.models import F

def employee_tree(request):
    nodes = Employee.objects.all()
    return render(request, 'employees/employee.html', {'nodes': nodes})