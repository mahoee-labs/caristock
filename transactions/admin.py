from django.contrib import admin

from transactions.models import Donation, DonationSupply, Pickup, PickupSupply


class DonationSupplyInline(admin.TabularInline):
    model = DonationSupply
    fields = [
        "supply",
        "quantity",
        "stock_quantity",
    ]


class PickupSupplyInline(admin.TabularInline):
    model = PickupSupply
    fields = [
        "supply",
        "quantity",
    ]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    """Let we manage donations"""

    list_filter = [
        "created",
        "updated",
    ]

    search_fields = [
        "donor__name",
        "donor__document",
    ]

    inlines = [DonationSupplyInline]


@admin.register(Pickup)
class PickupAdmin(admin.ModelAdmin):
    """Let we manage"""

    list_filter = [
        "created",
        "updated",
    ]

    search_fields = [
        "beneficiary__name",
        "beneficiary__document",
    ]

    inlines = [PickupSupplyInline]
