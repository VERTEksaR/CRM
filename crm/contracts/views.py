from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from contracts.models import Contract
from contracts.forms import ContractForm


class ContractListView(ListView):
    model = Contract
    queryset = Contract.objects.select_related('service').all()
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-list')


class ContractDetailsView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summa'] = context['object'].summa(context['object'].service.pk)
        return context


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-list')


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-edit.html'

    def get_success_url(self):
        return reverse_lazy('contracts:contracts-detail', kwargs={"pk": self.kwargs.get('pk')})

