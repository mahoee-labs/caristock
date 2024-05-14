from django.db import models

from caristock.base import LENGTH_CODE, LENGTH_EXTRA, LENGTH_REGULAR, ProjectModel


class DonorManager:
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Donor(ProjectModel):
    """Who is donating supplies"""

    name = models.CharField(
        help_text="Nome e sobrenome ou Nome da empresa",
        max_length=LENGTH_REGULAR,
    )
    address_1 = models.CharField(
        blank=True,
        help_text="Rua, número e complemento",
        max_length=LENGTH_EXTRA,
    )
    address_2 = models.CharField(
        blank=True,
        help_text="Bairro e cidade",
        max_length=LENGTH_EXTRA,
    )

    email = models.CharField(
        blank=True,
        help_text="Email do doador",
        max_length=LENGTH_REGULAR,
        unique=True,
    )
    document = models.CharField(
        blank=True,
        help_text="CPF ou CNPJ do doador",
        max_length=LENGTH_CODE,
        unique=True,
    )

    objects = DonorManager()

    def natural_key(self):
        return (self.name,)


class BeneficiaryManager:
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Beneficiary(ProjectModel):
    """Who is receiving supplies"""

    name = models.CharField(
        help_text="Nome e sobrenome",
        max_length=LENGTH_REGULAR,
    )
    document = models.CharField(
        help_text="CPF ou CNPJ do doador",
        max_length=LENGTH_CODE,
        unique=True,
    )
    photo = models.ImageField()

    objects = BeneficiaryManager()

    def natural_key(self):
        return (self.name,)
