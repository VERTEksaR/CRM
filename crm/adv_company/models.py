from django.db import models

from service.models import Service


class AdvCompany(models.Model):
    """Модель рекламной кампании"""
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    name = models.CharField(unique=True, max_length=255, verbose_name='Название компании')
    service = models.ManyToManyField(Service, verbose_name='Услуга')
    promotion_channel = models.CharField(max_length=127, verbose_name='Канал продвижения')
    budget = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Бюджет')

    def __str__(self):
        """Возвращает название рекламной кампании"""
        return self.name
