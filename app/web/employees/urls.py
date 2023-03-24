from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'employees'

urlpatterns = [
    path('', index, name='index'),

    path('tree/', employee_tree, name='tree'),
    path('list/', employee_list, name='list'),

    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='employees/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='employees/logged_out.html'), name='logout'),

    path('add/', create_employee, name='create_employee'),
    path('delete/', delete_employee, name='delete_employee'),
    path('update/', update_employee, name='update_employee'),
]