from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from service.models import Service
from adv_company.models import AdvCompany
from customers.models import Customer
from users.models import Lead
from users.mixins import GroupRequiredMixin


class MainPageView(View):
    """Класс для просмотра основной страницы"""
    @staticmethod
    def get(request: HttpRequest):
        """Метод для просмотра основной страницы"""
        products = Service.objects.all()
        advertisements = AdvCompany.objects.prefetch_related('service').all()
        leads = Lead.objects.select_related('ads').filter(is_active=False)
        customers = Customer.objects.select_related('lead', 'contract').all()
        context = {
            "products": products,
            "advertisements": advertisements,
            "leads": leads,
            "customers": customers,
        }
        return render(request, 'service/index.html', context=context)


class ServiceListView(ListView, GroupRequiredMixin):
    """Класс для просмотра всех услуг"""
    group_required = ["Маркетолог"]
    model = Service
    queryset = Service.objects.all()
    template_name = 'service/products-list.html'
    context_object_name = 'products'


class CreateServiceView(CreateView, GroupRequiredMixin):
    """Класс для создания новой услуги"""
    group_required = ["Маркетолог"]
    model = Service
    fields = ["name", "description", "price"]
    template_name = 'service/products-create.html'

    def get_success_url(self):
        return reverse_lazy('service:products-list')


class DeleteServiceView(DeleteView, GroupRequiredMixin):
    """Класс для удаления услуги"""
    group_required = ["Маркетолог"]
    model = Service
    template_name = 'service/products-delete.html'

    def get_success_url(self):
        return reverse_lazy('service:products-list')


class DetailsServiceView(DetailView, GroupRequiredMixin):
    """Класс для просмотра детальной информации об услуге"""
    group_required = ["Маркетолог"]
    model = Service
    template_name = 'service/products-detail.html'
    context_object_name = 'service'


class UpdateServiceView(UpdateView, GroupRequiredMixin):
    """Класс для обновления информации об услуге"""
    group_required = ["Маркетолог"]
    model = Service
    fields = ["name", "description", "price"]
    template_name = 'service/products-edit.html'

    def get_success_url(self):
        return reverse_lazy('service:products-detail', kwargs={"pk": self.kwargs.get('pk')})
