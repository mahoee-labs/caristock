from django.shortcuts import render
from inventory.models import Supply


def render_supply_select(request):
    query = request.GET.get("q", "")
    next = request.GET.get("n")
    results = list(Supply.objects.search(query))
    context = dict(
        query=query,
        results=results,
        count=len(results),
        next=next,
    )
    return render(request, "caristock/supply-select.html", context=context)
