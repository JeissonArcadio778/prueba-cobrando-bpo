from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Department
from employee.models import Employee

from employee.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return Employee.objects.all()
        else:
            return Employee.objects.filter(codigo=pk).first()
            # return Empleado.objects.filter(pk=self.request.user.profile.codigo)

    def list(self, request):
        empleado_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(empleado_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Employee successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            empleado_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if empleado_serializer.is_valid():
                empleado_serializer.save()
                return Response(empleado_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        empleado = self.get_queryset().filter(codigo=pk).first()
        if empleado:
            empleado.delete()
            return Response({"Message": "Employee successfully eliminated"}, status=status.HTTP_200_OK)
        return Response({"Message": "Employee doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
