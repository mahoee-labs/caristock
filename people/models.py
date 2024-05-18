from django.db import models

from caristock.base import LENGTH_CODE, LENGTH_EXTRA, LENGTH_REGULAR, ProjectModel
from django.utils.translation import gettext_lazy as _


class DonorManager(models.Manager):
    def search(self, query):
        if query:
            name_matches = models.Q(name__contains=query)
            document_matches = models.Q(document__contains=query)
            return self.filter(name_matches | document_matches)
        else:
            return self.all()[:20]

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Donor(ProjectModel):
    """Who is donating supplies"""

    name = models.CharField(
        help_text=_("Donor's full name"),
        max_length=LENGTH_REGULAR,
        verbose_name=_("Name"),
    )
    address_1 = models.CharField(
        blank=True,
        help_text=_("Street address, including number and any additional details"),
        max_length=LENGTH_EXTRA,
        verbose_name=_("Address 1"),
    )
    address_2 = models.CharField(
        blank=True,
        help_text=_("Neighborhood and city"),
        max_length=LENGTH_EXTRA,
        verbose_name=_("Address 2"),
    )

    email = models.CharField(
        blank=True,
        help_text=_("Email address of the donor"),
        max_length=LENGTH_REGULAR,
        unique=True,
        verbose_name=_("Email"),
    )
    document = models.CharField(
        blank=True,
        help_text=_("Donor's CPF or CNPJ"),
        max_length=LENGTH_CODE,
        unique=True,
        verbose_name=_("Document"),
    )

    objects = DonorManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Donor")
        verbose_name_plural = _("Donors")


class BeneficiaryManager(models.Manager):
    def search(self, query):
        if query:
            name_matches = models.Q(name__contains=query)
            document_matches = models.Q(document__contains=query)
            return self.filter(name_matches | document_matches)
        else:
            return self.all()[:20]

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Beneficiary(ProjectModel):
    """Who is receiving supplies"""

    name = models.CharField(
        help_text=_("Beneficiary's full name"),
        max_length=LENGTH_REGULAR,
        verbose_name=_("Name"),
    )
    document = models.CharField(
        help_text=_("Beneficiary's CPF or CNPJ"),
        max_length=LENGTH_CODE,
        unique=True,
        verbose_name=_("Document"),
    )
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to="images/beneficiary_photos/",
        verbose_name=_("Photo"),
    )

    objects = BeneficiaryManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Beneficiary")
        verbose_name_plural = _("Beneficiaries")
