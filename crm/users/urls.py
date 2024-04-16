from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .views import (
    LeadListView,
    LeadCreateView,
    LeadDetailsView,
    LeadUpdateView,
    LeadDeleteView,
    MyLogoutView,
)

app_name = 'users'

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='leads-list'),
    path('leads/<int:pk>/', LeadDetailsView.as_view(), name='leads-detail'),
    path('leads/<int:pk>/edit/', LeadUpdateView.as_view()),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view()),
    path('leads/new/', LeadCreateView.as_view()),

    path('accounts/logout/', MyLogoutView.as_view()),
    path('accounts/login/',
         LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True, next_page='/'),
         name='login'),
]
