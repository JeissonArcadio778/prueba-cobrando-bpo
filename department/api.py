from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):

    permission_classes = []
    serializer_class = DepartmentSerializer

    def get_queryset(self, pk):

        if pk == None:
            return Department.objects.all()
        
        else:
            return Department.objects.filter(idCode=pk).first()

    def list(self, request):

        department_serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(department_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Department created"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def update(self, request, pk):

        if self.get_queryset(pk):
            department_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            
            if department_serializer.is_valid():
                department_serializer.save()
                return Response(department_serializer.data, status=status.HTTP_200_OK)
            
            return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):

        department = self.get_queryset().filter(idCode=pk).first()

        if department:
            department.delete()
            return Response({"Message": "Department successfully eliminated!"}, status=status.HTTP_200_OK)
        
        return Response({"Message": "Department doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
