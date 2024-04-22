from django.urls import path

from service.views import (
    MainPageView,
    ServiceListView,
    CreateServiceView,
    DeleteServiceView,
    DetailsServiceView,
    UpdateServiceView,
)


app_name = "service"

urlpatterns = [
    path("", MainPageView.as_view(), name="base"),
    path("products/", ServiceListView.as_view(), name="products-list"),
    path("products/<int:pk>/", DetailsServiceView.as_view(), name="products-detail"),
    path("products/new/", CreateServiceView.as_view()),
    path("products/<int:pk>/edit/", UpdateServiceView.as_view()),
    path("products/<int:pk>/delete/", DeleteServiceView.as_view()),
]
