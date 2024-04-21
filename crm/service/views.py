from typing import List

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from service.models import Service
from adv_company.models import AdvCompany
from customers.models import Customer
from users.models import Lead
from users.mixins import GroupRequiredMixin


def add_group_and_permissions():
    names: List[str] = ['Оператор', 'Менеджер', 'Маркетолог', 'Администратор']
    permissions = [["add_lead", "change_lead", "delete_lead", "view_lead"],
                   ["add_contract", "change_contract", "delete_contract", "view_contract",
                    "view_lead", "add_customer", "view_customer"],
                   ["add_service", "change_service", "delete_service", "view_service",
                    "add_advcompany", "change_advcompany", "delete_advcompany", "view_advcompany"],
                   ["add_user", "change_user", "delete_user", "view_user",
                    "add_permission", "change_permission", "view_permission", "delete_permission"]]

    for name in names:
        new_group, created = Group.objects.get_or_create(name=name)

        if created:
            if name == 'Оператор':
                for perm in range(4):
                    permission = Permission.objects.get(codename=permissions[0][perm])
                    new_group.permissions.add(permission)
            elif name == 'Менеджер':
                for perm in range(7):
                    permission = Permission.objects.get(codename=permissions[1][perm])
                    new_group.permissions.add(permission)
            elif name == 'Маркетолог':
                for perm in range(8):
                    permission = Permission.objects.get(codename=permissions[2][perm])
                    new_group.permissions.add(permission)
            elif name == 'Администратор':
                for perm in range(8):
                    permission = Permission.objects.get(codename=permissions[3][perm])
                    new_group.permissions.add(permission)


class MainPageView(View):
    """Класс для просмотра основной страницы"""

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        """Метод для просмотра основной страницы"""
        add_group_and_permissions()
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
    group_required: list[str] = ["Маркетолог"]
    model = Service
    queryset = Service.objects.all()
    template_name: str = 'service/products-list.html'
    context_object_name: str = 'products'


class CreateServiceView(CreateView, GroupRequiredMixin):
    """Класс для создания новой услуги"""
    group_required: list[str] = ["Маркетолог"]
    model = Service
    fields: list[str] = ["name", "description", "price"]
    template_name: str = 'service/products-create.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('service:products-list')


class DeleteServiceView(DeleteView, GroupRequiredMixin):
    """Класс для удаления услуги"""
    group_required: list[str] = ["Маркетолог"]
    model = Service
    template_name: str = 'service/products-delete.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('service:products-list')


class DetailsServiceView(DetailView, GroupRequiredMixin):
    """Класс для просмотра детальной информации об услуге"""
    group_required: list[str] = ["Маркетолог"]
    model = Service
    template_name: str = 'service/products-detail.html'
    context_object_name: str = 'service'


class UpdateServiceView(UpdateView, GroupRequiredMixin):
    """Класс для обновления информации об услуге"""
    group_required: list[str] = ["Маркетолог"]
    model = Service
    fields: list[str] = ["name", "description", "price"]
    template_name: str = 'service/products-edit.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('service:products-detail', kwargs={"pk": self.kwargs.get('pk')})
