from django.core.exceptions import ValidationError
from django.db import models

from adv_company.models import AdvCompany


class Lead(models.Model):
    """Класс лида"""

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    first_name = models.CharField(max_length=63, verbose_name="Имя")
    last_name = models.CharField(max_length=63, verbose_name="Фамилия")
    phone = models.CharField(unique=True, max_length=11, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Почта")
    ads = models.ForeignKey(
        AdvCompany, on_delete=models.PROTECT, verbose_name="Рекламная кампания"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активный пользователь")

    def __str__(self):
        """Возвращает фамилию и имя лида"""
        return f"{self.last_name} {self.first_name}"

    def clean(self):
        if len(self.first_name) > 63:
            raise ValidationError('Длина имени не может превышать 63 символов')

        if len(self.last_name) > 63:
            raise ValidationError('Длина фамилии не может превышать 63 символов')

        if len(self.phone) != 11:
            raise ValidationError('Номер телефона должен состоять из 11 цифр')
        else:
            for element in self.phone:
                if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise ValidationError('Номер телефона должен состоять только из цифр')

        if '@' not in self.email:
            raise ValidationError('В адресе почты обязательно должен присутствовать знак "@"')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
