from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from caristock.utils import get_param, get_param_int
from people.forms import DonorForm
from people.models import Donor


def render_select_donor(request):
    query = request.GET.get("q")
    next = request.GET.get("n")
    if not next:
        messages.warning(request, "The 'next' argument is missing.")
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
    return render(request, "caristock/select_donor.html", context=context)


def render_show_donor(request):
    donor_id = get_param_int(request, "donor", 0)
    next = get_param(request, "n")
    donor = get_object_or_404(Donor, pk=donor_id)
    if request.method == "POST":
        form = DonorForm(request.POST)
    else:
        form = DonorForm(instance=donor)
    context = dict(
        next=next,
        form=form,
        donor=donor,
    )
    return render(request, "caristock/show_donor.html", context=context)
