from django.db import models

from users.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    class Meta:
        verbose_name = 'Активный пользователь'
        verbose_name_plural = 'Активные пользователи'

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.lead
