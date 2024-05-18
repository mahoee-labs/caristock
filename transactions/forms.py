from django import forms

from transactions.models import DonationSupply


class DonationSupplyForm(forms.ModelForm):
    class Meta:
        model = DonationSupply
        fields = ["quantity"]
