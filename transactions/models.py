from django.db import models

from caristock.base import ProjectModel


class DonationManager:
    def get_by_natural_key(self, name):
        return self.get(donor__name=name)


class Donation(ProjectModel):
    donor = models.ForeignKey(
        "people.Donor",
        help_text="Quem irá doar",
        on_delete=models.PROTECT,
    )

    def natural_key(self):
        return (self.donor.name,)


class DonationSupply(ProjectModel):
    donation = models.ForeignKey(
        "Donation",
        on_delete=models.PROTECT,
    )
    supply = models.ForeignKey(
        "inventory.Supply",
        on_delete=models.PROTECT,
        help_text="Item de doação a ser recebido",
    )

    quantity = models.IntegerField(
        help_text="Quantidade a ser recebida do item de doação",
    )

    class Meta:
        unique_together = (("donation", "supply"),)


class PickupManager:
    def get_by_natural_key(self, name):
        return self.get(beneficiary__name=name)


class Pickup(ProjectModel):
    beneficiary = models.ForeignKey(
        "people.Beneficiary",
        help_text="Quem receberá a doação",
        on_delete=models.PROTECT,
    )

    def natural_key(self):
        return (self.beneficiary.name,)


class PickupSupply(ProjectModel):
    pickup = models.ForeignKey(
        "Pickup",
        on_delete=models.PROTECT,
    )
    supply = models.ForeignKey(
        "inventory.Supply",
        help_text="Item de doação a ser entregue",
        on_delete=models.PROTECT,
    )

    quantity = models.IntegerField(
        help_text="Quantidade a ser entregue do item de doação",
    )

    class Meta:
        unique_together = (("pickup", "supply"),)
