from django.urls import path, include
from .views import StudentViewSet, UniversityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('university', UniversityViewSet, basename='university')
router.register('students', StudentViewSet, basename='students')

urlpatterns =[
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]