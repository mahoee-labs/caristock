from django.contrib import messages
from django.shortcuts import render

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
