from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from server.api.v1.user.serializers import (
    UserRegisterSerializer,
    UserSerializer,
    TokenObtainPairResponseSerializer
)
from server.apps.user.models import User


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class DecoratedTokenObtainPairView(TokenObtainPairView):
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
            description='Пользователь успешно зарегистрирован',
            examples={
                'application/json': {
                        "id": 0,
                        "login": "userlogin",
                        "name": "username",
                    }
                }
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
