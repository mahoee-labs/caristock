from django.db import models
from django.utils.translation import gettext_lazy as _

LENGTH_CODE = 20
LENGTH_REGULAR = 80
LENGTH_EXTRA = 255


class ProjectModel(models.Model):
    """Base class for models in this project"""

    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_("When this record was created"),
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text=_("When this record was updated"),
    )

    class Meta:
        abstract = True
