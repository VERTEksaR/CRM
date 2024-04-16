from django.urls import path

from .views import (
    AdvListView,
    AdvCreateView,
    AdvDetailView,
    AdvUpdateView,
    AdvDeleteView,
    AdvStatistics,
)

app_name = 'advcompany'

urlpatterns = [
    path('ads/', AdvListView.as_view(), name='adv-list'),
    path('ads/<int:pk>/', AdvDetailView.as_view(), name='adv-edit'),
    path('ads/<int:pk>/edit/', AdvUpdateView.as_view()),
    path('ads/<int:pk>/delete/', AdvDeleteView.as_view()),
    path('ads/new/', AdvCreateView.as_view()),
    path('ads/statistic/', AdvStatistics.as_view()),
]
