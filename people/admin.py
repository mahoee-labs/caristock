from django.contrib import admin

from people.models import Beneficiary, Donor


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
