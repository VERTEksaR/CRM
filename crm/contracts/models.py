from django.db import models
from django.utils import timezone

from service.models import Service


class Contract(models.Model):
    """Модель контракта"""
    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    name = models.CharField(unique=True, max_length=255, verbose_name='Название контракта')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='Услуга')
    file = models.FileField(upload_to='contracts/documents/', verbose_name='Файл')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата заключения')
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=1),
                                verbose_name='Дата расторжения')

    @staticmethod
    def summa(pk):
        """Метод summa для вывода стоимости услуги, указанной в контракте"""
        product = Service.objects.get(id=pk)
        return product.price

    def __str__(self):
        """Возвращает название контракта"""
        return self.name
