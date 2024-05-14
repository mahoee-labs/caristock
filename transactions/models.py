from django.db import models

from caristock.base import ProjectModel
from django.utils.translation import gettext_lazy as _


class DonationManager:
    def get_by_natural_key(self, name):
        return self.get(donor__name=name)


class Donation(ProjectModel):
    donor = models.ForeignKey(
        "people.Donor",
        help_text=_("Who is donating"),
        on_delete=models.PROTECT,
        verbose_name=_("Donor"),
    )

    def natural_key(self):
        return (self.donor.name,)

    def __str__(self):
        return f"{self.donor.name} #{self.id}"

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")


class DonationSupply(ProjectModel):
    donation = models.ForeignKey(
        "Donation",
        on_delete=models.PROTECT,
    )
    supply = models.ForeignKey(
        "inventory.Supply",
        on_delete=models.PROTECT,
        help_text=_("Donated item to be received"),
        verbose_name=_("Supply"),
    )

    quantity = models.IntegerField(
        help_text=_("Quantity of donated item to be received"),
        verbose_name=_("Quantity"),
    )

    class Meta:
        verbose_name = _("Supply Donation")
        verbose_name_plural = _("Supply Donations")
        unique_together = (("donation", "supply"),)


class PickupManager:
    def get_by_natural_key(self, name):
        return self.get(beneficiary__name=name)


class Pickup(ProjectModel):
    beneficiary = models.ForeignKey(
        "people.Beneficiary",
        help_text=_("Donation recipient"),
        on_delete=models.PROTECT,
        verbose_name=_("Beneficiary"),
    )

    def natural_key(self):
        return (self.beneficiary.name,)

    def __str__(self):
        return f"{self.beneficiary.name} #{self.id}"

    class Meta:
        verbose_name = _("Pickup")
        verbose_name_plural = _("Pickups")


class PickupSupply(ProjectModel):
    pickup = models.ForeignKey(
        "Pickup",
        on_delete=models.PROTECT,
    )
    supply = models.ForeignKey(
        "inventory.Supply",
        help_text=_("Donated item to be delivered"),
        on_delete=models.PROTECT,
        verbose_name=_("Supply"),
    )

    quantity = models.IntegerField(
        help_text=_("Quantity of donated item to be delivered"),
        verbose_name=_("Quantity"),
    )

    def __str__(self):
        return self.supply.name

    class Meta:
        verbose_name = _("Supply Pickup")
        verbose_name_plural = _("Supply Pickups")
        unique_together = (("pickup", "supply"),)
