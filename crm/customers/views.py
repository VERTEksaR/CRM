from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from customers.models import Customer
from users.models import Lead
from users.mixins import GroupRequiredMixin


class CustomerListView(ListView, GroupRequiredMixin):
    """Класс для просмотра всех активных пользователей"""
    group_required: list[str] = ["Менеджер"]
    model = Customer
    template_name: str = 'customers/customers-list.html'
    context_object_name: str = 'customers'

    def get_queryset(self):
        leads = Lead.objects.select_related('ads').all()
        customers = Customer.objects.select_related('lead', 'contract').all()

        for customer in customers:
            if customer.lead in leads and not customer.lead.is_active:
                lead = leads.get(id=customer.lead.id)
                lead.is_active = True
                lead.save()

        return customers


class CustomerCreateView(CreateView):
    """Класс для создания нового активного пользователя"""
    model = Customer
    fields: list[str] = ['lead', 'contract']
    template_name: str = 'customers/customers-create.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        lead_id = request.POST['lead']
        lead = Lead.objects.select_related('ads').get(id=lead_id)
        customers = Customer.objects.select_related('lead', 'contract').all()
        self.get(request, *args, **kwargs)

        for customer in customers:
            if customer.lead == lead:
                messages.error(request, 'Данный пользователь уже является акивным')
                return render(request, self.template_name, self.get_context_data())
        super().post(request, *args, **kwargs)
        return redirect('/customers/')

    def get_success_url(self) -> HttpResponse:
        return reverse('customers:customers-list')


class CustomerDetailView(DetailView):
    """Класс для просмотра детальной инфомрации об активном пользователе"""
    model = Customer
    template_name: str = 'customers/customers-detail.html'
    context_object_name: str = 'customer'


class CustomerDeleteView(DeleteView):
    """Класс для удаления активного пользователя"""
    model = Customer
    template_name: str = 'customers/customers-delete.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        customer = Customer.objects.select_related('lead', 'contract').get(id=kwargs['pk'])
        lead = Lead.objects.select_related('ads').get(id=customer.lead.pk)
        lead.is_active = False
        lead.save()
        super().post(request, *args, **kwargs)
        return redirect('/customers/')

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('customers:customers-list')


class CustomerUpdateView(UpdateView):
    """Класс для обновления информации об активном пользователе"""
    model = Customer
    fields: list[str] = ["lead"]
    template_name: str = 'customers/customers-edit.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('customers:customers-detail', kwargs={"pk": self.kwargs.get('pk')})
