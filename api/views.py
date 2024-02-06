from rest_framework import viewsets, permissions, status, views, mixins, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination

from .models import (
    Category,
    Task
)

from .serializers import (
    CategorySerializer,
    TaskSerializer,
    RegisterSerializer,
    UserSerializer
)


class ApiFilterSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 90


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    pagination_class = ApiFilterSetPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    @swagger_auto_schema(
        operation_description="List all categories",
        responses={200: CategorySerializer(many=True)},
        security=[],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a category",
        request_body=CategorySerializer,
        responses={201: CategorySerializer(many=False)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a category",
        responses={200: CategorySerializer(many=False)},
        security=[],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a category",
        request_body=CategorySerializer,
        responses={200: CategorySerializer(many=False)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial update a category",
        request_body=CategorySerializer,
        responses={200: CategorySerializer(many=False)},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a category",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    pagination_class = ApiFilterSetPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    @swagger_auto_schema(
        operation_description="List all tasks",
        responses={200: TaskSerializer(many=True)},
        security=[],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a task",
        request_body=TaskSerializer,
        responses={201: TaskSerializer(many=False)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a task",
        responses={200: TaskSerializer(many=False)},
        security=[],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a task",
        request_body=TaskSerializer,
        responses={200: TaskSerializer(many=False)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial update a task",
        request_body=TaskSerializer,
        responses={200: TaskSerializer(many=False)},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a task",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User was successfully created!",
        })
