from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from customers.models import Customer
from users.models import Lead


class LeadListView(ListView, PermissionRequiredMixin):
    """Класс для просмотра всех лидов"""
    permission_required: str = 'users.view_lead'
    model = Lead
    template_name: str = 'users/leads-list.html'
    context_object_name: str = 'leads'

    def get_queryset(self):
        leads = Lead.objects.select_related('ads').all()
        customers = Customer.objects.select_related('lead', 'contract').all()

        for customer in customers:
            if customer.lead in leads and not customer.lead.is_active:
                lead = leads.get(id=customer.lead.id)
                lead.is_active = True
                lead.save()

        queryset_leads = leads.filter(is_active=False)
        return queryset_leads


class LeadCreateView(CreateView, PermissionRequiredMixin):
    """Класс для создания нового лида"""
    permission_required: str = 'users.add_lead'
    model = Lead
    fields: list[str] = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name: str = 'users/leads-create.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('users:leads-list')


class LeadDetailsView(DetailView, PermissionRequiredMixin):
    """Класс для просмотра подробной информации о лиде"""
    permission_required: str = 'users.view_lead'
    model = Lead
    template_name: str = 'users/leads-detail.html'


class LeadUpdateView(UpdateView, PermissionRequiredMixin):
    """Класс для обновления информации о лиде"""
    permission_required: str = 'users.change_lead'
    model = Lead
    fields: list[str] = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name: str = 'users/leads-edit.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('users:leads-detail', kwargs={'pk': self.kwargs.get('pk')})


class LeadDeleteView(DeleteView, PermissionRequiredMixin):
    """Класс для удаления лида"""
    permission_required: str = 'users.delete_lead'
    model = Lead
    template_name: str = 'users/leads-delete.html'

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy('users:leads-list')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('service:base')
