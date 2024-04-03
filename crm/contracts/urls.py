from django.urls import path

from contracts.views import (
    ContractListView,
    ContractCreateView,
    ContractDeleteView,
    ContractDetailsView,
    ContractUpdateView,
)


app_name = 'contracts'

urlpatterns = [
    path('contracts/', ContractListView.as_view(), name='contracts-list'),
    path('contracts/<int:pk>/', ContractDetailsView.as_view(), name='contracts-detail'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view()),
    path('contracts/<int:pk>/edit/', ContractUpdateView.as_view()),
    path('contracts/new/', ContractCreateView.as_view()),
]
