from django.db import models
from caristock.base import LENGTH_REGULAR, ProjectModel
from django.utils.translation import gettext_lazy as _


class SupplyManager(models.Manager):
    def search(self, query):
        if query:
            name_matches = models.Q(name__icontains=query)
            return self.filter(name_matches)
        else:
            return self.all()[:20]

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Supply(ProjectModel):
    """To register donated supplies"""

    name = models.CharField(
        max_length=LENGTH_REGULAR,
        unique=True,
        help_text=_("Enter the donated item name"),
        verbose_name=_("Name"),
    )

    objects = SupplyManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Supply")
        verbose_name_plural = _("Supplies")


class StockManager:
    def get_by_natural_key(self, name):
        return self.get(supply__name=name)


class Stock(ProjectModel):
    """Inventory of donated items"""

    supply = models.OneToOneField(
        "Supply",
        on_delete=models.PROTECT,
        verbose_name=_("Supply"),
    )

    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
    )

    objects = StockManager()

    def natural_key(self):
        return (self.supply.name,)

    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stock")
