from django.urls import path
from django.views.generic import TemplateView

from service.views import (
    ServiceListView,
    CreateServiceView,
    DeleteServiceView,
    DetailsServiceView,
    UpdateServiceView,
)


app_name = 'service'

urlpatterns = [
    path('', TemplateView.as_view(template_name='service/_base.html')),
    path('products/', ServiceListView.as_view(), name='products-list'),
    path('products/<int:pk>/', DetailsServiceView.as_view(), name='products-detail'),
    path('products/new/', CreateServiceView.as_view()),
    path('products/<int:pk>/edit/', UpdateServiceView.as_view()),
    path('products/<int:pk>/delete/', DeleteServiceView.as_view()),
]
