from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from contracts.models import Contract
from contracts.forms import ContractForm
from users.mixins import GroupRequiredMixin


class ContractListView(ListView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Contract
    queryset = Contract.objects.select_related('service').all()
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(CreateView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-list')


class ContractDetailsView(DetailView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Contract
    template_name = 'contracts/contracts-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summa'] = context['object'].summa(context['object'].service.pk)
        return context


class ContractDeleteView(DeleteView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Contract
    template_name = 'contracts/contracts-delete.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-list')


class ContractUpdateView(UpdateView, GroupRequiredMixin):
    group_required = ["Менеджер"]
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-edit.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-detail', kwargs={"pk": self.kwargs.get('pk')})

