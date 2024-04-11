from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from server.api.v1.user.serializers import (
    UserRegisterSerializer,
    UserSerializer,
    TokenObtainPairResponseSerializer
)
from server.apps.user.models import User


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None
    http_method_names = ['get', 'post', 'put', 'patch']


    @swagger_auto_schema(
        operation_description="Получение профиля пользователя",
        responses={
            200: UserSerializer,
        },
    )
    def list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    """
    Переопределенный view для корректного отображения в сваггере
    """
    # noinspection PyTypeChecker
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserCreateViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )

    @swagger_auto_schema(responses={
        '201': openapi.Response(
            description='',
            examples={
                'application/json': {
                        "id": 0,
                        "email": "user@example.com"
                    }
                }
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
