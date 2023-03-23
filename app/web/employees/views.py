from django.shortcuts import render
from .models import Employee
from django.db.models import Q


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