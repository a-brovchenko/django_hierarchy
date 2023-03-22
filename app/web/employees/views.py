from django.shortcuts import render
from .models import Employee


def employee_tree(request):
    employees = Employee.objects.filter(parent=None)
    return render(request, 'employees/employee.html', {'nodes': employees})
