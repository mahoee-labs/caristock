from django.shortcuts import render, get_object_or_404

from people.forms import BeneficiaryForm, DonorForm
from people.models import Donor, Beneficiary


def render_donor_select(request):
    query = request.GET.get("q", "")
    next = request.GET.get("n")
    found = list(Donor.objects.search(query))
    search_results = dict(
        count=len(found),
        donors=found,
    )
    context = dict(
        query=query,
        next=next,
        search_results=search_results,
    )
    return render(request, "caristock/donor-select.html", context=context)


def render_donor_show(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    next = request.GET.get("n")
    if request.method == "POST":
        form = DonorForm(request.POST)
    else:
        form = DonorForm(instance=donor)
    context = dict(
        next=next,
        form=form,
        donor=donor,
    )
    return render(request, "caristock/donor-show.html", context=context)


def render_donor_edit(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    next = request.GET.get("n")
    if request.method == "POST":
        form = DonorForm(request.POST)
    else:
        form = DonorForm(instance=donor)
    context = dict(
        next=next,
        form=form,
        donor=donor,
    )
    return render(request, "caristock/donor-edit.html", context=context)


def render_beneficiary_select(request):
    query = request.GET.get("q", "")
    next = request.GET.get("n")
    found = list(Beneficiary.objects.search(query))
    search_results = dict(
        count=len(found),
        beneficiaries=found,
    )
    context = dict(
        query=query,
        next=next,
        search_results=search_results,
    )
    return render(request, "caristock/beneficiary-select.html", context=context)


def render_beneficiary_show(request, beneficiary_id):
    beneficiary = get_object_or_404(Beneficiary, pk=beneficiary_id)
    next = request.GET.get("n")
    if request.method == "POST":
        form = BeneficiaryForm(request.POST)
    else:
        form = BeneficiaryForm(instance=beneficiary)
    context = dict(
        next=next,
        form=form,
        beneficiary=beneficiary,
    )
    return render(request, "caristock/beneficiary-show.html", context=context)


def render_beneficiary_edit(request, donor_id):
    beneficiary = get_object_or_404(Beneficiary, pk=donor_id)
    next = request.GET.get("n")
    if request.method == "POST":
        form = BeneficiaryForm(request.POST)
    else:
        form = BeneficiaryForm(instance=beneficiary)
    context = dict(
        next=next,
        form=form,
        beneficiary=beneficiary,
    )
    return render(request, "caristock/beneficiary-edit.html", context=context)
