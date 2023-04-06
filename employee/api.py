from rest_framework import viewsets, status
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer


    def get_queryset(self, pk):

        if pk == None:
            return Employee.objects.all()
        
        else:
            return Employee.objects.filter(idCode=pk).first()



    def list(self, request):

        employee_serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(employee_serializer.data, status=status.HTTP_200_OK)



    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Employee created"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def update(self, request, pk):

        if self.get_queryset(pk):
            employee_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response(employee_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):

        employee = self.get_queryset().filter(idCode=pk).first()

        if employee:
            employee.delete()
            return Response({"Message": "Employee eliminated"}, status=status.HTTP_200_OK)
        
        return Response({"Message": "Employee doesn't exist in Data Base"}, status=status.HTTP_400_BAD_REQUEST)
