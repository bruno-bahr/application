from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('main_screen/', views.main_screen, name="main_screen"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('employees/', views.employees, name="employees"),
    path('employee/add', views.employee_add, name="employee_add"),
    path('employee/del/', views.employee_del, name="employee_del"),
    path('employee/delete/<int:employee_pk>', views.employee_delete, name="employee_delete"),
    path('employee/edit/', views.employee_edit, name="employee_edit"),
    path('employee/update/<int:employee_pk>', views.employee_update, name="employee_update")
]   