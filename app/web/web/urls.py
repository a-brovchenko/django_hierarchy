from django.contrib import admin
from django.urls import path
from employees.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', employee_tree),

]
