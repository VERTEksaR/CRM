from django.test import TestCase
from django.urls import reverse

from service.models import Service
from adv_company.models import AdvCompany
from users.models import Lead


class LeadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='test', description='test', price='1.00')

        adv_company = AdvCompany.objects.create(name='test', promotion_channel='test',
                                                budget='1.00')
        adv_company.service.set((service,))
        ads = AdvCompany.objects.get(pk=1)

        Lead.objects.create(first_name='test', last_name='test',
                            phone='12345678909', email='test@test.com',
                            ads=ads)

    def test_first_name_label(self):
        lead = Lead.objects.get(pk=1)
        field_label = lead._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_first_name_length(self):
        lead = Lead.objects.get(pk=1)
        max_length = lead._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 63)

    def test_last_name_label(self):
        lead = Lead.objects.get(pk=1)
        field_label = lead._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_last_name_length(self):
        lead = Lead.objects.get(pk=1)
        max_length = lead._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 63)

    def test_phone_label(self):
        lead = Lead.objects.get(pk=1)
        field_label = lead._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Номер телефона')

    def test_phone_max_length(self):
        lead = Lead.objects.get(pk=1)
        max_length = lead._meta.get_field('phone').max_length
        self.assertEquals(max_length, 11)

    def test_phone_is_unique(self):
        lead = Lead.objects.get(pk=1)
        unique = lead._meta.get_field('phone').unique
        self.assertTrue(unique)

    def test_email_label(self):
        lead = Lead.objects.get(pk=1)
        field_label = lead._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Почта')

    def test_email_is_unique(self):
        lead = Lead.objects.get(pk=1)
        unique = lead._meta.get_field('email').unique
        self.assertTrue(unique)

    def test_ads_label(self):
        lead = Lead.objects.get(pk=1)
        field_label = lead._meta.get_field('ads').verbose_name
        self.assertEquals(field_label, 'Рекламная кампания')


class LeadListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='test', description='test', price='1.00')

        adv_company = AdvCompany.objects.create(name='test', promotion_channel='test',
                                                budget='1.00')
        adv_company.service.set((service,))
        ads = AdvCompany.objects.get(pk=1)

        Lead.objects.create(first_name='test', last_name='test',
                            phone='12345678909', email='test@test.com',
                            ads=ads)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/leads/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('users:leads-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('users:leads-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'users/leads-list.html')

    def test_lists_all_authors(self):
        resp = self.client.get(reverse('users:leads-list'))
        self.assertEqual(resp.status_code, 200)


class LeadCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/leads/new/')
        self.assertEqual(resp.status_code, 200)

    def test_view_post_lead_data(self):
        service = Service.objects.create(name='test', description='test', price='1.00')

        ads = AdvCompany.objects.create(name='test', promotion_channel='test',
                                        budget='1.00')
        ads.service.set((service,))
        resp = self.client.post('/leads/new/', {"first_name": "test",
                                                "last_name": "test",
                                                "phone": "1345678909",
                                                "email": "test@test.com",
                                                "ads": ads})
        self.assertEqual(resp.status_code, 200)
