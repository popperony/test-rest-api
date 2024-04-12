from django.db import models


class Palette(models.Model):
    user = models.ForeignKey(to="user.User", on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='Название палитры')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    class Meta:
        verbose_name = 'Палитра'
        verbose_name_plural = 'Палитры'

    def __str__(self):
        return str(self.id)


class Color(models.Model):
    palette = models.ForeignKey(to=Palette, on_delete=models.CASCADE, verbose_name='Палитра')
    hex_code = models.CharField(max_length=7, verbose_name='HEX-код цвета')
    name = models.CharField(max_length=25, verbose_name='Название цвета', blank=True, null=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.hex_code
