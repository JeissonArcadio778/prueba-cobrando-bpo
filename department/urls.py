from rest_framework import routers
from .api import DepartmentViewset

router = routers.DefaultRouter()

router.register(r'departments', DepartmentViewset, basename='departments')

urlpatterns = router.urls
