from django.shortcuts import render, get_object_or_404

from caristock.utils import get_param, get_param_int
from people.forms import DonorForm
from people.models import Donor


def render_donor_select(request):
    query = request.GET.get("q")
    next = request.GET.get("n")
    if query:
        found = list(Donor.objects.search(query))
        search_results = dict(
            count=len(found),
            donors=found,
        )
    else:
        search_results = None
    context = dict(
        query=query,
        next=next,
        search_results=search_results,
    )
    return render(request, "caristock/donor-select.html", context=context)


def render_donor_show(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    next = get_param(request, "n")
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
    next = get_param(request, "n")
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
