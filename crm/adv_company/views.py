from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView


from adv_company.models import AdvCompany
from .serializers import AdvSerializer


class AdvListView(ListView):
    model = AdvCompany
    queryset = AdvCompany.objects.prefetch_related('service').all()
    # serializer_class = AdvSerializer
    template_name = 'adv/ads-list.html'
    context_object_name = 'ads'


class AdvCreateView(CreateView):
    model = AdvCompany
    fields = ["name", "service", "promotion_channel", "budget"]
    template_name = 'adv/ads-create.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-list')


class AdvDetailView(DetailView):
    model = AdvCompany
    template_name = 'adv/ads-detail.html'


class AdvUpdateView(UpdateView):
    model = AdvCompany
    fields = ["name", "service", "promotion_channel", "budget"]
    template_name = 'adv/ads-edit.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-edit', kwargs={"pk": self.kwargs.get('pk')})


class AdvDeleteView(DeleteView):
    model = AdvCompany
    template_name = 'adv/ads-delete.html'

    def get_success_url(self):
        return reverse_lazy('advcompany:adv-list')
