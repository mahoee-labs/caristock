from django.db import models
from caristock.base import LENGTH_REGULAR, ProjectModel


class SupplyManager:
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Supply(ProjectModel):
    """To register donated supplies"""

    name = models.CharField(
        max_length=LENGTH_REGULAR,
        unique=True,
        help_text="Insira o nome do item doado",
    )

    objects = SupplyManager()

    def natural_key(self):
        return (self.name,)


class StockManager:
    def get_by_natural_key(self, name):
        return self.get(supply__name=name)


class Stock(ProjectModel):
    """Inventory of donated items"""

    supply = models.ForeignKey(
        "Supply",
        on_delete=models.PROTECT,
        unique=True,
    )

    quantity = models.IntegerField()

    objects = StockManager()

    def natural_key(self):
        return (self.supply.name,)
