from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Form, Response
from .serializers import FormSerializer, ResponseSerializer
from .permissions import IsTeacherOrReadOnly, IsOwnerOrReadOnly
from .pagination import CustomPageNumberPagination

class FormViewSet(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'description', 'questions']
    search_fields = ['id', 'title', 'description', 'questions']
    ordering_fields = ['id', 'title', 'description', 'questions']

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Form.objects.all()
        return Form.objects.filter(class_group__students=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsOwnerOrReadOnly]  # Use custom permission
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'form', 'student', 'submitted_at', 'answers']
    search_fields = ['id', 'form', 'student', 'submitted_at', 'answers']
    ordering_fields = ['id', 'form', 'student', 'submitted_at', 'answers']

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Response.objects.all()
        return Response.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
