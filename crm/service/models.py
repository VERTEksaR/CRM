from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    name = models.CharField(unique=True, max_length=255, verbose_name='Название услуги')
    description = models.TextField(blank=True, null=True, max_length=1023, verbose_name='Описание услуги')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена услуги')

    def __str__(self):
        return self.name
