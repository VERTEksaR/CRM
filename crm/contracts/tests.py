from django.test import TestCase

from service.models import Service
from contracts.models import Contract


class LeadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='test', description='test', price='1.00')

        Contract.objects.create(name='test', service=service,
                                file='__init__.py')

    def test_name_label(self):
        contract = Contract.objects.get(pk=1)
        field_label = contract._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название контракта')

    def test_name_max_length(self):
        contract = Contract.objects.get(pk=1)
        max_length = contract._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_name_is_unique(self):
        contract = Contract.objects.get(pk=1)
        unique = contract._meta.get_field('name').unique
        self.assertTrue(unique)

    def test_service_label(self):
        contract = Contract.objects.get(pk=1)
        field_label = contract._meta.get_field('service').verbose_name
        self.assertEquals(field_label, 'Услуга')

    def test_file_label(self):
        contract = Contract.objects.get(pk=1)
        field_label = contract._meta.get_field('file').verbose_name
        self.assertEquals(field_label, 'Файл')

    def test_start_date_label(self):
        contract = Contract.objects.get(pk=1)
        field_label = contract._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'Дата заключения')

    def test_end_date_label(self):
        contract = Contract.objects.get(pk=1)
        field_label = contract._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'Дата расторжения')

    def test_summa(self):
        service = Service.objects.get(pk=1)
        self.assertEquals(service.price, 1.00)
