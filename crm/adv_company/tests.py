from django.test import TestCase

from service.models import Service
from adv_company.models import AdvCompany


class LeadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='test', description='test', price='1.00')

        adv_company = AdvCompany.objects.create(name='test', promotion_channel='test',
                                                budget='1.00')
        adv_company.service.set((service,))

    def test_name_label(self):
        adv_company = AdvCompany.objects.get(pk=1)
        field_label = adv_company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название компании')

    def test_name_max_length(self):
        adv_company = AdvCompany.objects.get(pk=1)
        max_length = adv_company._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_name_is_unique(self):
        adv_company = AdvCompany.objects.get(pk=1)
        unique = adv_company._meta.get_field('name').unique
        self.assertTrue(unique)

    def test_service_label(self):
        adv_company = AdvCompany.objects.get(pk=1)
        field_label = adv_company._meta.get_field('service').verbose_name
        self.assertEquals(field_label, 'Услуга')

    def test_promotion_channel_label(self):
        adv_company = AdvCompany.objects.get(pk=1)
        field_label = adv_company._meta.get_field('promotion_channel').verbose_name
        self.assertEquals(field_label, 'Канал продвижения')

    def test_promotion_channel_length(self):
        adv_company = AdvCompany.objects.get(pk=1)
        max_length = adv_company._meta.get_field('promotion_channel').max_length
        self.assertEquals(max_length, 127)

    def test_budget_label(self):
        adv_company = AdvCompany.objects.get(pk=1)
        field_label = adv_company._meta.get_field('budget').verbose_name
        self.assertEquals(field_label, 'Бюджет')

    def test_budget_max_digits(self):
        adv_company = AdvCompany.objects.get(pk=1)
        max_digits = adv_company._meta.get_field('budget').max_digits
        self.assertEquals(max_digits, 8)

    def test_budget_decimal_places(self):
        adv_company = AdvCompany.objects.get(pk=1)
        decimal_places = adv_company._meta.get_field('budget').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_budget_default(self):
        adv_company = AdvCompany.objects.get(pk=1)
        default = adv_company._meta.get_field('budget').default
        self.assertEquals(default, 0)
