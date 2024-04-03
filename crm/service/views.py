from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from service.models import Service
from adv_company.models import AdvCompany
from users.models import Lead


class MainPageView(View):
    @staticmethod
    def get(request: HttpRequest):
        products = Service.objects.all()
        advertisements = AdvCompany.objects.prefetch_related('service').all()
        leads = Lead.objects.select_related('ads').all()
        context = {
            "products": products,
            "advertisements": advertisements,
            "leads": leads,
        }
        return render(request, 'service/index.html', context=context)


class ServiceListView(ListView):
    model = Service
    queryset = Service.objects.all()
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
