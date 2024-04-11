from django.contrib.auth.password_validation import validate_password as django_validate
from django.core.validators import ValidationError
from rest_framework import serializers


def validate_password(value):
    """
    Функция валидации пароля встроенными средствами Django, указанных в settings в AUTH_PASSWORD_VALIDATORS
    :param value:
    :return value:
    """
    try:
        django_validate(value)
    except ValidationError as error:
        raise serializers.ValidationError(detail={'error': error})

    return value
