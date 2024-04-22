from django import forms

from contracts.models import Contract


class ContractForm(forms.ModelForm):
    """Форма контракта"""

    class Meta:
        model = Contract
        fields = ["name", "service", "file", "start_date", "end_date"]

    start_date = forms.DateField()
    end_date = forms.DateField()
