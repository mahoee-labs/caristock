from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from inventory.models import Supply
from people.models import Donor
from transactions.forms import DonationSupplyForm
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


def render_donation_build(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    context = dict(
        donation=donation,
    )
    return render(request, "caristock/donation-build.html", context=context)


def render_donationsupply_create(request):
    next = request.GET.get("n")
    donation_id = request.GET.get("donation")
    supply_id = request.GET.get("supply")
    donation = Donation.objects.filter(pk=donation_id).first()
    supply = Supply.objects.filter(pk=supply_id).first()
    donationsupply, _ = DonationSupply.objects.get_or_create(
        donation=donation, supply=supply, defaults=dict(quantity=1)
    )
    redirect_url = reverse("donationsupply-edit", args=[donationsupply.id])
    return redirect(redirect_url + "?n=" + next)


def render_donationsupply_edit(request, donationsupply_id):
    next = request.GET.get("n")
    donationsupply = get_object_or_404(DonationSupply, pk=donationsupply_id)
    if request.method == "POST":
        form = DonationSupplyForm(request.POST, instance=donationsupply)
        if form.is_valid():
            donationsupply = form.save()
            if next:
                return redirect(next)
    else:
        form = DonationSupplyForm(instance=donationsupply)
    context = dict(
        next=next,
        form=form,
        donationsupply=donationsupply,
    )
    return render(request, "caristock/donationsupply-edit.html", context=context)


def render_donationsupply_delete(request, donationsupply_id):
    next = request.GET.get("n", "/")
    DonationSupply.objects.filter(pk=donationsupply_id).delete()
    return redirect(next)
