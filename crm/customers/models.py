from django.db import models

from users.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    """Модель активного пользователя"""

    class Meta:
        verbose_name = "Активный пользователь"
        verbose_name_plural = "Активные пользователи"

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, verbose_name='Пользователь')
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True,
                                 verbose_name='Контракт')

    def __str__(self):
        return f"{self.lead} | {self.contract}"
