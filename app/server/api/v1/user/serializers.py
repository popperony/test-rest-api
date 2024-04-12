from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.api.v1.utils import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'login',
            'name',
            'date_joined',
        )
        read_only_fields = (
            'id',
            'date_joined',
        )


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class UserRegisterSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'login', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}

    def create(self, validated_data):
        check_user = User.objects.filter(login=validated_data['login']).first()
        if check_user:
            raise ValidationError(detail={'error': 'Такой пользователь уже существует'})

        user = User.objects.create_user(
            login=validated_data['login'],
            name=validated_data['name'],
            password=validate_password(validated_data['password'])
        )
        return user
