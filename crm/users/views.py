from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from customers.models import Customer
from users.mixins import GroupRequiredMixin
from users.models import Lead


class LeadListView(ListView, GroupRequiredMixin):
    """Класс для просмотра всех лидов"""
    group_required = ["Оператор", "Менеджер"]
    model = Lead
    template_name = 'users/leads-list.html'
    context_object_name = 'leads'

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


class LeadCreateView(CreateView, GroupRequiredMixin):
    """Класс для создания нового лида"""
    group_required = ["Оператор"]
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-create.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')


class LeadDetailsView(DetailView, GroupRequiredMixin):
    """Класс для просмотра подробной информации о лиде"""
    group_required = ["Оператор"]
    model = Lead
    template_name = 'users/leads-detail.html'


class LeadUpdateView(UpdateView, GroupRequiredMixin):
    """Класс для обновления информации о лиде"""
    group_required = ["Оператор"]
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-edit.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-detail', kwargs={'pk': self.kwargs.get('pk')})


class LeadDeleteView(DeleteView, GroupRequiredMixin):
    """Класс для удаления лида"""
    group_required = ["Оператор"]
    model = Lead
    template_name = 'users/leads-delete.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('service:base')
