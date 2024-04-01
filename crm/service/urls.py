from django.urls import path
from django.views.generic import TemplateView

from service.views import (
    ServicesAPIView,
    ServiceAPIView,
    CreateServiceAPIView,
    create_service,
)


app_name = 'service'

urlpatterns = [
    path('', ServicesAPIView.as_view(), name='services'),
    # path('create/', CreateServiceAPIView.as_view(), name='service_create'),
    path('<int:pk>/', ServiceAPIView.as_view(), name='service_detail'),

    path('create/', create_service)
]
