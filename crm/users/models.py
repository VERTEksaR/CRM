from django.contrib.auth.models import User
from django.db import models

from adv_company.models import AdvCompany


def get_currencies():
    return {
        ("Администратор", "Администратор"),
        ("Оператор", "Оператор"),
        ("Маркетолог", "Маркетолог"),
        ("Менеджер", "Менеджер"),
    }


class Lead(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    first_name = models.CharField(max_length=63, verbose_name='Имя')
    last_name = models.CharField(max_length=63, verbose_name='Фамилия')
    phone = models.IntegerField(unique=True, verbose_name='Номер телефона')
    email = models.EmailField(unique=True, verbose_name='Почта')
    ads = models.ForeignKey(AdvCompany, on_delete=models.PROTECT, verbose_name='Рекламная кампания')
    is_active = models.BooleanField(default=False, verbose_name='Активный пользователь')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
