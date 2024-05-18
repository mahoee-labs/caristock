from django.shortcuts import get_object_or_404, render
from inventory.forms import QuantityForm, SupplyForm
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


def render_supply_show(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)
    next = request.GET.get("n")
    quantity = request.GET.get("quantity", 1)
    form = SupplyForm(instance=supply)
    extra_form = QuantityForm(initial={"quantity": quantity})
    context = dict(
        next=next,
        supply=supply,
        form=form,
        extra_form=extra_form,
    )
    return render(request, "caristock/supply-show.html", context=context)
