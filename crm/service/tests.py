from django.test import TestCase

from service.models import Service


class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Service.objects.create(name='test', description='test', price='1.00')

    def test_name_label(self):
        service = Service.objects.get(pk=1)
        field_label = service._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название услуги')

    def test_name_max_length(self):
        service = Service.objects.get(pk=1)
        max_length = service._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_name_is_unique(self):
        service = Service.objects.get(pk=1)
        unique = service._meta.get_field('name').unique
        self.assertTrue(unique)

    def test_description_label(self):
        service = Service.objects.get(pk=1)
        field_label = service._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание услуги')

    def test_description_max_length(self):
        service = Service.objects.get(pk=1)
        max_length = service._meta.get_field('description').max_length
        self.assertEquals(max_length, 1023)

    def test_description_blank(self):
        service = Service.objects.get(pk=1)
        blank = service._meta.get_field('description').blank
        self.assertTrue(blank)

    def test_description_null(self):
        service = Service.objects.get(pk=1)
        null = service._meta.get_field('description').null
        self.assertTrue(null)

    def test_price_label(self):
        service = Service.objects.get(pk=1)
        field_label = service._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Цена услуги')

    def test_price_max_digits(self):
        service = Service.objects.get(pk=1)
        max_digits = service._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 8)

    def test_price_decimal_places(self):
        service = Service.objects.get(pk=1)
        decimal_places = service._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_price_default(self):
        service = Service.objects.get(pk=1)
        default = service._meta.get_field('price').default
        self.assertEquals(default, 0)

