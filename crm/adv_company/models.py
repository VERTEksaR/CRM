from django.core.exceptions import ValidationError
from django.db import models

from service.models import Service


class AdvCompany(models.Model):
    """Модель рекламной кампании"""

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    name = models.CharField(
        unique=True, max_length=255, verbose_name="Название компании"
    )
    service = models.ManyToManyField(Service, verbose_name="Услуга")
    promotion_channel = models.CharField(
        max_length=127, verbose_name="Канал продвижения"
    )
    budget = models.DecimalField(
        default=0, max_digits=8, decimal_places=2, verbose_name="Бюджет"
    )

    def __str__(self):
        """Возвращает название рекламной кампании"""
        return self.name

    def clean(self):
        """Валидация данных"""
        if len(self.name) > 255:
            raise ValidationError('Длина названия не может превышать 255 символов')

        if len(self.promotion_channel) > 127:
            raise ValidationError('Длина канала продвижения не может превышать 127 символов')

        if self.budget < 0 or self.budget > 99999999.99:
            raise ValidationError('Бюджет должен быть в диапазоне 0.00 - 99,999,999.00')

    def save(self, *args, **kwargs):
        """Метод для сохранения данных при успешной валидации"""
        self.full_clean()
        return super().save(*args, **kwargs)
