from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.contrib.auth.mixins import PermissionRequiredMixin

from contracts.models import Contract
from contracts.forms import ContractForm


class ContractListView(ListView, PermissionRequiredMixin):
    """Класс для просмотра всех контрактов"""

    permission_required: str = "contracts.view_contract"
    model = Contract
    queryset = Contract.objects.select_related("service").all()
    template_name: str = "contracts/contracts-list.html"
    context_object_name: str = "contracts"


class ContractCreateView(CreateView, PermissionRequiredMixin):
    """Класс для создание нового контракта"""

    permission_required: str = "contracts.add_contract"
    model = Contract
    form_class = ContractForm
    template_name: str = "contracts/contracts-create.html"

    def get_success_url(self):
        return reverse_lazy("contracts:contracts-list")


class ContractDetailsView(DetailView, PermissionRequiredMixin):
    """Класс для просмотра детальной информации контракта"""

    permission_required: str = "contracts.view_contract"
    model = Contract
    template_name: str = "contracts/contracts-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["summa"] = context["object"].summa(context["object"].service.pk)
        return context


class ContractDeleteView(DeleteView, PermissionRequiredMixin):
    """Класс для удаления контракта"""

    permission_required: str = "contracts.delete_contract"
    model = Contract
    template_name: str = "contracts/contracts-delete.html"

    def get_success_url(self):
        return reverse_lazy("contracts:contracts-list")


class ContractUpdateView(UpdateView, PermissionRequiredMixin):
    """Класс для обновления информации о контракте"""

    permission_required: str = "contracts.change_contract"
    model = Contract
    form_class = ContractForm
    template_name: str = "contracts/contracts-edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "contracts:contracts-detail", kwargs={"pk": self.kwargs.get("pk")}
        )
