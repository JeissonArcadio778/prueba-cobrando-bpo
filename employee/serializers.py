from rest_framework import serializers
from .models import Employee
from department.serializers import DepartmentSerializer


class EmployeeSerializer(serializers.ModelSerializer):

    serializer_class = DepartmentSerializer

    class Meta:
        model = Employee
        fields = ('idCode', 'nif', 'name', 'lastname1', 'lastname2', 'idCode_department')
        read_only_fields = ('idCode')