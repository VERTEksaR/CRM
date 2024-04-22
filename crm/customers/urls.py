from django.urls import path

from customers.views import (
    CustomerListView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerDeleteView,
    CustomerUpdateView,
)


app_name = "customers"

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customers-list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customers-detail"),
    path("customers/<int:pk>/delete/", CustomerDeleteView.as_view()),
    path("customers/<int:pk>/edit/", CustomerUpdateView.as_view()),
    path("customers/new/", CustomerCreateView.as_view()),
]
