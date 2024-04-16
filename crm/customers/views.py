from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from customers.models import Customer
from users.mixins import GroupRequiredMixin


class CustomerListView(ListView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Customer
    queryset = Customer.objects.select_related('lead', 'contract')
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['lead', 'contract']
    template_name = 'customers/customers-create.html'

    def get_success_url(self):
        return reverse_lazy('customers:customers-list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    context_object_name = 'customer'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'

    def get_success_url(self):
        return reverse_lazy('customers:customers-list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ["lead"]
    template_name = 'customers/customers-edit.html'

    def get_success_url(self):
        return reverse_lazy('customers:customers-detail', kwargs={"pk": self.kwargs.get('pk')})

