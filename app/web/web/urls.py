from django.contrib import admin
from django.urls import path
from employees.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tree/', employee_tree),
    path('list/', employee_list),
]
