from faker import Faker
from employees.models import Employee


fake = Faker()

ceo = Employee.objects.create(
    name='CEO',
    position='CEO',
    email=fake.email(),
    employment_date=fake.date_this_decade(),
)

for i in range(1, 11):
    employee = Employee.objects.create(
        name=fake.name(),
        position=fake.job()[0:20],
        email=fake.email(),
        employment_date=fake.date_this_decade(),
    )

    parent = ceo if i == 1 else Employee.objects.filter(id__lt=employee.id).order_by('?').first()
    employee.parent = parent
    employee.save()




