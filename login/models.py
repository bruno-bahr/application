from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    document_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True, default='email@email.com')
    department = models.CharField(max_length=40)
    def __str__(self):
        return self.name

