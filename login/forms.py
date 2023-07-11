from django import forms
from django.conf import settings
from login.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ()
