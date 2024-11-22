from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  SchoolViewSet, ClassViewSet, StudentViewSet, get_schools

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'students', StudentViewSet)

# the API are now determined by the router
urlpatterns = [
    path('', include(router.urls)),
]