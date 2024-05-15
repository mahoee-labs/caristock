from django.shortcuts import render

from transactions.models import Donation


def render_home(request):
    context = dict(
        overview_highest_count=123,
        overview_lowest_count=-9,
        incoming_donations=Donation.objects.all(),
    )
    return render(request, "caristock/home.html", context)
