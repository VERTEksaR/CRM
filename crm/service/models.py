from django.core.exceptions import ValidationError
from django.db import models


class Service(models.Model):
    """Модель услуги"""

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    name = models.CharField(unique=True, max_length=255, verbose_name="Название услуги")
    description = models.TextField(
        blank=True, null=True, max_length=1023, verbose_name="Описание услуги"
    )
    price = models.DecimalField(
        default=0, max_digits=8, decimal_places=2, verbose_name="Цена услуги"
    )

    def __str__(self):
        """Возвращает название услуги"""
        return self.name

    def clean(self):
        """Валидация данных"""
        if len(self.name) > 255:
            raise ValidationError('Длина названия не может превышать 255 символов')

        if len(self.description) > 1023:
            raise ValidationError('Длина описания не может превышать 1023 символов')

        if self.price < 0 or self.price > 99999999.99:
            raise ValidationError('Цена должна быть в диапазоне 0.00 - 99,999,999.00')

    def save(self, *args, **kwargs):
        """Метод для сохранения данных при успешной валидации"""
        self.full_clean()
        return super().save(*args, **kwargs)
