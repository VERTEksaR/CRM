from django.urls import path

from .views import (
    LeadListView,
    LeadCreateView,
    LeadDetailsView,
    LeadUpdateView,
    LeadDeleteView,
)

app_name = 'users'

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='leads-list'),
    path('leads/<int:pk>/', LeadDetailsView.as_view(), name='leads-detail'),
    path('leads/<int:pk>/edit/', LeadUpdateView.as_view()),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view()),
    path('leads/new/', LeadCreateView.as_view()),
]
