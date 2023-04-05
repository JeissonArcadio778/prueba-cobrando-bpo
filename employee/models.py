from django.db import models
from department.models import Department


# Create your models here.

from django.db import models

class Employee(models.Model):
    """ Template for the Employee table """
    idCode = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    idCode_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAd = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['idCode']

    def __str__(self):
        return f'{self.name} {self.lastname1} - {self.lastname2} - {self.idCode_department}'
