from django.urls import path

from authentication.views import (
    login_view,
    logout_view,
)

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view),
    path('accounts/logout/', logout_view),
]
