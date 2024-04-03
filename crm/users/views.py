from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from users.models import Lead


class LeadListView(ListView):
    model = Lead
    queryset = Lead.objects.select_related('ads').all()
    template_name = 'users/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(CreateView):
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-create.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')


class LeadDetailsView(DetailView):
    model = Lead
    template_name = 'users/leads-detail.html'


class LeadUpdateView(UpdateView):
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ads']
    template_name = 'users/leads-edit.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-detail', kwargs={'pk': self.kwargs.get('pk')})


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'users/leads-delete.html'

    def get_success_url(self):
        return reverse_lazy('users:leads-list')
