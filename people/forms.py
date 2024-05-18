from django import forms

from people.models import Donor, Beneficiary


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ["name", "address_1", "address_2", "email", "document"]


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ["name", "document", "photo"]
