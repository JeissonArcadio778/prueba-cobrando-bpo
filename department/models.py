from django.db import models


class Department(models.Model):

    idCode = models.AutoField(primary_key=True)

    name = models.CharField(max_length=80)
    
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    

    class Meta:
        verbose_name = 'Department'

        verbose_name_plural = 'Departments'

        ordering = ['idCode']

    def __str__(self):
        return f'{self.name} {self.idCode}'
