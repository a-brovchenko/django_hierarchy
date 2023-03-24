from django.contrib import admin
from employees.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls', namespace='employees')),
]
