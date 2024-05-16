from django.db import models

from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from caristock.base import LENGTH_CODE, ProjectModel
from django.utils.translation import gettext_lazy as _

from inventory.models import Stock


class DonationManager:
    def get_by_natural_key(self, name):
        return self.get(donor__name=name)


class Donation(ProjectModel):
    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", _("In Progress")
        COMPLETED = "completed", _("Completed")
        CANCELLED = "cancelled", _("Cancelled")

    donor = models.ForeignKey(
        "people.Donor",
        help_text=_("Who is donating"),
        on_delete=models.PROTECT,
        verbose_name=_("Donor"),
    )
    status = models.CharField(
        choices=Status,
        default=Status.IN_PROGRESS,
        help_text=_("Approval Status"),
        max_length=LENGTH_CODE,
    )

    def natural_key(self):
        return (self.donor.name,)

    def __str__(self):
        return f"{self.donor.name} #{self.id}"

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")


@receiver(post_save, sender=Donation)
def update_stock_after_donation(sender, instance, **kwargs):
    for current in instance.donationsupply_set.all():
        current.save()


class DonationSupply(ProjectModel):
    donation = models.ForeignKey(
        "Donation",
        on_delete=models.CASCADE,
    )
    supply = models.ForeignKey(
        "inventory.Supply",
        on_delete=models.CASCADE,
        help_text=_("Donated item to be received"),
        verbose_name=_("Supply"),
    )

    quantity = models.IntegerField(
        help_text=_("Quantity of donated item to be received"),
        verbose_name=_("Quantity"),
    )

    stock_quantity = models.IntegerField(
        default=0,
        # editable=False,
    )

    class Meta:
        verbose_name = _("Donation Supply")
        verbose_name_plural = _("Donation Supplies")
        unique_together = (("donation", "supply"),)

    def update_stock(self):
        delta = self.stock_quantity - self.quantity
        if delta:
            stock = Stock.objects.get(supply=self.supply)
            stock.quantity -= delta
            stock.save()
            self.stock_quantity = self.quantity
            self.save()

    def clear_stock(self):
        if self.stock_quantity:
            stock = Stock.objects.get(supply=self.supply)
            stock.quantity -= self.stock_quantity
            stock.save()
            self.stock_quantity = 0
            self.save()


@receiver(post_save, sender=DonationSupply)
def update_stock_after_donationsupply(sender, instance, **kwargs):
    if instance.donation.status == Donation.Status.COMPLETED:
        instance.update_stock()
    else:
        instance.clear_stock()


@receiver(pre_delete, sender=DonationSupply)
def clear_stock_after_donationsupply(sender, instance, **kwargs):
    instance.clear_stock()


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
        verbose_name = _("Pickup Supply")
        verbose_name_plural = _("Pickup Supplies")
        unique_together = (("pickup", "supply"),)
