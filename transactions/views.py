from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _

from inventory.models import Supply
from people.models import Donor
from transactions.models import Donation, DonationSupply


def render_donation_create(request):
    donor_id = request.GET.get("donor")
    donor = Donor.objects.filter(pk=donor_id).first()
    if donor is None:
        messages.error(request, _("Could not find donor record"))
        donation = None
    else:
        donation = Donation.objects.create(donor=donor)
    context = dict(
        donor=donor,
        donation=donation,
    )
    return render(request, "caristock/donation-create.html", context=context)


def render_donation_add(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    supply_id = request.GET.get("s")
    quantity = int(request.GET.get("quantity", 1))
    supply = Supply.objects.filter(pk=supply_id).first()
    if supply is None:
        messages.error(request, _("Could not find selected supply."))
    else:
        obj, created = DonationSupply.objects.update_or_create(
            donation=donation,
            supply=supply,
            defaults=dict(
                quantity=quantity,
            ),
        )
        if not created:
            messages.info(request, _("Updated supply quantity"))

    return redirect("donation-build", donation.id)


def render_donation_delete(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    supply_id = request.GET.get("s")
    supply = Supply.objects.filter(pk=supply_id).first()
    if supply is None:
        messages.error(request, _("Could not find selected supply."))
    else:
        DonationSupply.objects.filter(donation=donation, supply=supply).delete()

    return redirect("donation-build", donation.id)


def render_donation_build(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    context = dict(
        donation=donation,
    )
    return render(request, "caristock/donation-build.html", context=context)
