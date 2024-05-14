from django.contrib import admin

from people.models import Beneficiary, Donor
from transactions.models import Donation, Pickup


class PickupInline(admin.TabularInline):
    model = Pickup
    extra = 0


class DonationInline(admin.TabularInline):
    model = Donation
    extra = 0


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    """Let we manage donors"""

    list_display = [
        "name",
        "document",
        "address_1",
        "email",
    ]

    list_filter = [
        "created",
        "updated",
    ]

    search_fields = [
        "name",
        "address_1",
        "address_2",
        "email",
        "document",
    ]

    inlines = [DonationInline]


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    """Let we manage beneficiaries"""

    list_display = [
        "name",
        "document",
    ]

    list_filter = [
        "created",
        "updated",
    ]

    search_fields = [
        "name",
        "document",
    ]

    inlines = [PickupInline]
