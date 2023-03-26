from faker import Faker
from employees.models import Employee
import os
from dotenv import load_dotenv

fake = Faker()
load_dotenv(dotenv_path="../.env")


#create ceo employee
ceo = Employee.objects.create(
    name='Chief Head',
    position='CEO',
    email=fake.email(),
    employment_date=fake.date_this_decade(),
)

employees_num = os.getenv("EMPLOYEES_NUM")

if not employees_num:
    employees_num = 200
else:
    employees_num = int(employees_num)

# other employee
for i in range(1, employees_num):
    employee = Employee.objects.create(
        name=fake.name(),
        position=fake.job()[0:20],
        email=fake.email(),
        employment_date=fake.date_this_decade(),
    )
    #random choice parent
    if i == 1:
        parent = ceo
    else:
        descendants = employee.get_descendants(include_self=True)
        parent = Employee.objects.exclude(id__in=descendants).order_by('?').first()
    employee.parent = parent
    employee.save()




