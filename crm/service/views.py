from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from service.models import Service
from .serializers import ServiceSerializer


class ServiceListView(ListView):
    model = Service
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    template_name = 'service/products-list.html'
    context_object_name = 'products'


class CreateServiceView(CreateView):
    model = Service
    fields = ["name", "description", "price"]
    template_name = 'service/products-create.html'

    def get_success_url(self):
        return reverse_lazy('service:products-list')


class DeleteServiceView(DeleteView):
    model = Service
    template_name = 'service/products-delete.html'
    success_url = '/products/'

    def get_success_url(self):
        return reverse_lazy('service:products-list')


class DetailsServiceView(DetailView):
    model = Service
    template_name = 'service/products-detail.html'
    context_object_name = 'service'


class UpdateServiceView(UpdateView):
    model = Service
    fields = ["name", "description", "price"]
    template_name = 'service/products-edit.html'

    def get_success_url(self):
        return reverse_lazy('service:products-detail', kwargs={"pk": self.kwargs.get('pk')})
