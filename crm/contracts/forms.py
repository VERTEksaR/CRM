from django import forms

from contracts.models import Contract

from crm.settings import DATE_INPUT_FORMATS


class ContractForm(forms.ModelForm):
    """Форма контракта"""

    class Meta:
        model = Contract
        fields = ["name", "service", "file", "start_date", "end_date"]

    start_date = forms.DateField(input_formats=DATE_INPUT_FORMATS)
    end_date = forms.DateField(input_formats=DATE_INPUT_FORMATS)
