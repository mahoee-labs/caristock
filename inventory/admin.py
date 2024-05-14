from django.contrib import admin

from inventory.models import Stock, Supply
from django.db.models import Q


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    """Let we manage supplies"""

    list_display = [
        "name",
    ]

    search_fields = [
        "name",
    ]

    list_filter = [
        "created",
        "updated",
    ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """Let we manage the inventory"""

    list_display = [
        "supply",
        "quantity",
    ]

    search_fields = [
        "supply__name",
    ]

    list_filter = [
        "created",
        "updated",
    ]
