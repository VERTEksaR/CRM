from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.core.exceptions import ObjectDoesNotExist


from adv_company.models import AdvCompany
from customers.models import Customer
from users.models import Lead
from users.mixins import GroupRequiredMixin


class AdvListView(ListView, GroupRequiredMixin):
    """Класс для просмотра списка всех рекламных кампаний"""
    group_required = ["Маркетолог"]
    model = AdvCompany
    queryset = AdvCompany.objects.prefetch_related('service').all()
    template_name = 'adv/ads-list.html'
    context_object_name = 'ads'


class AdvCreateView(CreateView, GroupRequiredMixin):
    """Класс для создания новой рекламной кампании"""
    group_required = ["Маркетолог"]
    model = AdvCompany
    fields = ["name", "service", "promotion_channel", "budget"]
    template_name = 'adv/ads-create.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-list')


class AdvDetailView(DetailView, GroupRequiredMixin):
    """Класс для просмотра подробной информации рекламной кампании"""
    group_required = ["Маркетолог"]
    model = AdvCompany
    template_name = 'adv/ads-detail.html'


class AdvUpdateView(UpdateView, GroupRequiredMixin):
    """Класс для обновления информации о рекламной кампании"""
    group_required = ["Маркетолог"]
    model = AdvCompany
    fields = ["name", "service", "promotion_channel", "budget"]
    template_name = 'adv/ads-edit.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-edit', kwargs={"pk": self.kwargs.get('pk')})


class AdvDeleteView(DeleteView, GroupRequiredMixin):
    """Класс для удаления рекламной кампании"""
    group_required = ["Маркетолог"]
    model = AdvCompany
    template_name = 'adv/ads-delete.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-list')


class AdvStatistics(View):
    """Класс для отображения статистики рекламных кампаний"""
    @staticmethod
    def get(request: HttpRequest):
        """Метод get выводит статистику рекламных кампаний"""
        count = 0

        ads = AdvCompany.objects.prefetch_related('service').all()
        all_leads = Lead.objects.select_related('ads').all()
        all_customers = Customer.objects.select_related('lead', 'contract').all()

        for ad in ads:
            leads = all_leads.filter(ads=ad)
            count += 1
            customers, price = 0, 0

            for lead in leads:
                try:
                    ss = all_customers.get(lead=lead)
                    price += ss.contract.service.price
                    customers += 1
                except ObjectDoesNotExist:
                    pass
            leads = all_leads.filter(ads=ad).count()
            ad.leads = leads
            ad.customers = customers
            ad.profit = price - ad.budget
        context = {
            "ads": ads
        }
        return render(request, 'adv/ads-statistic.html', context=context)
