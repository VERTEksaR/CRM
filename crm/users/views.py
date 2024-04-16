from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from users.models import Lead
from users.mixins import GroupRequiredMixin


class LeadListView(ListView, GroupRequiredMixin):
    group_required = ["Оператор", "Менеджер"]
    model = Lead
    queryset = Lead.objects.select_related('ads').all()
    template_name = 'users/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(CreateView, GroupRequiredMixin):
    group_required = ["Оператор"]
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-create.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')


class LeadDetailsView(DetailView, GroupRequiredMixin):
    group_required = ["Оператор"]
    model = Lead
    template_name = 'users/leads-detail.html'


class LeadUpdateView(UpdateView, GroupRequiredMixin):
    group_required = ["Оператор"]
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-edit.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-detail', kwargs={'pk': self.kwargs.get('pk')})


class LeadDeleteView(DeleteView, GroupRequiredMixin):
    group_required = ["Оператор"]
    model = Lead
    template_name = 'users/leads-delete.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('service:base')
