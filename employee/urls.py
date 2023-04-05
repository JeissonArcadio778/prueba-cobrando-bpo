from rest_framework import routers
from .api import EmployeeViewSet

router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = router.urls
