from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from users.models import Lead
from customers.models import Customer
from users.mixins import GroupRequiredMixin


class CustomerListView(ListView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'

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
    model = Customer
    fields = ['lead', 'contract']
    template_name = 'customers/customers-create.html'

    def post(self, request, *args, **kwargs):
        lead_id = request.POST['lead']
        lead = Lead.objects.select_related('ads').get(id=lead_id)
        customers = Customer.objects.select_related('lead', 'contract').all()

        for customer in customers:
            if customer.lead == lead:
                messages.error(request, 'Данный пользователь уже является акивным')
                return render(request, self.template_name, self.get_context_data())
        super().post(request, *args, **kwargs)
        return redirect('/customers/')


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

