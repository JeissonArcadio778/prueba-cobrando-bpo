from rest_framework import serializers
from .models import Department 
from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('idCode', 'name', 'budget')

