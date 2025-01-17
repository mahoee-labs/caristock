"""
URL configuration for caristock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from caristock.views import render_home
from inventory.views import render_supply_select, render_supply_show
from people.views import (
    render_beneficiary_edit,
    render_beneficiary_select,
    render_beneficiary_show,
    render_donor_select,
    render_donor_edit,
    render_donor_show,
)
from transactions.views import (
    render_donation_build,
    render_donation_create,
    render_donationsupply_create,
    render_donationsupply_edit,
    render_donationsupply_delete,
    render_pickup_create,
)


urlpatterns = [
    path("", render_home),
    path("donor/select", render_donor_select, name="donor-select"),
    path("donor/<int:donor_id>/show", render_donor_show, name="donor-show"),
    path("donor/<int:donor_id>/edit", render_donor_edit, name="donor-edit"),
    path("beneficiary/select", render_beneficiary_select, name="beneficiary-select"),
    path(
        "beneficiary/<int:beneficiary_id>/show",
        render_beneficiary_show,
        name="beneficiary-show",
    ),
    path(
        "beneficiary/<int:beneficiary_id>/edit",
        render_beneficiary_edit,
        name="beneficiary-edit",
    ),
    path("supply/select", render_supply_select, name="supply-select"),
    path("supply/<int:supply_id>/show", render_supply_show, name="supply-show"),
    path("donation/create", render_donation_create, name="donation-create"),
    path(
        "donation/<int:donation_id>/build", render_donation_build, name="donation-build"
    ),
    path("pickup/create", render_pickup_create, name="pickup-create"),
    path(
        "donationsupply/create",
        render_donationsupply_create,
        name="donationsupply-create",
    ),
    path(
        "donationsupply/<int:donationsupply_id>/edit",
        render_donationsupply_edit,
        name="donationsupply-edit",
    ),
    path(
        "donationsupply/<int:donationsupply_id>/delete",
        render_donationsupply_delete,
        name="donationsupply-delete",
    ),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
