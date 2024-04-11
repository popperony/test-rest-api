from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser):
    login = models.CharField(max_length=150,verbose_name='Логин', unique=True)
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login
