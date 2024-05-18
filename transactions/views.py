from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _

from people.models import Donor, Beneficiary
from transactions.models import Donation, Pickup


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


def render_donation_build(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    context = dict(
        donation=donation,
    )
    return render(request, "caristock/donation-build.html", context=context)


def render_pickup_create(request):
    beneficiary_id = request.GET.get("beneficiary")
    beneficiary = Beneficiary.objects.filter(pk=beneficiary_id).first()
    if beneficiary is None:
        messages.error(request, _("Could not find beneficiary record"))
        pickup = None
    else:
        pickup = Pickup.objects.create(beneficiary=beneficiary)
    context = dict(
        beneficiary=beneficiary,
        pickup=pickup,
    )
    return render(request, "caristock/pickup-create.html", context=context)
