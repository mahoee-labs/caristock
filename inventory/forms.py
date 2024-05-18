from django import forms

from inventory.models import Supply


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["name"]


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1)
