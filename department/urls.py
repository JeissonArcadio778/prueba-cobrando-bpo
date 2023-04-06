from rest_framework import routers
from .api import DepartmentViewSet

router = routers.DefaultRouter()

router.register(r'departments', DepartmentViewSet, basename='departments')

urlpatterns = router.urls
