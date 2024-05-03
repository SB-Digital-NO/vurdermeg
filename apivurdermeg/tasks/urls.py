from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import FormViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet, basename='forms')
router.register(r'responses', ResponseViewSet, basename='responses')

urlpatterns = [
    path('', include(router.urls)),  # This line includes all the CRUD operations for forms and responses
]
