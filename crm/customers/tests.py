from django.test import TestCase

from service.models import Service
from adv_company.models import AdvCompany
from users.models import Lead
from contracts.models import Contract
from customers.models import Customer


class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='test', description='test', price='1.00')

        adv_company = AdvCompany.objects.create(name='test', promotion_channel='test',
                                                budget='1.00')
        adv_company.service.set((service,))
        ads = AdvCompany.objects.get(pk=1)

        lead = Lead.objects.create(first_name='test', last_name='test',
                                   phone='12345678909', email='test@test.com',
                                   ads=ads)

        contract = Contract.objects.create(name='test', service=service,
                                           file='__init__.py')

        Customer.objects.create(lead=lead, contract=contract)

    def test_lead_label(self):
        customer = Customer.objects.get(pk=1)
        field_label = customer._meta.get_field('lead').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_contract_label(self):
        customer = Customer.objects.get(pk=1)
        field_label = customer._meta.get_field('contract').verbose_name
        self.assertEquals(field_label, 'Контракт')

    def test_contract_is_null(self):
        customer = Customer.objects.get(pk=1)
        null = customer._meta.get_field('contract').null
        self.assertTrue(null)

