from datetime import datetime

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(_("book title"), max_length=200, unique=True)
    published_at = models.PositiveIntegerField(
        _("year of publication"),
        default=datetime.now().year,
        validators=[
            validators.MinValueValidator(1455),
            validators.MaxValueValidator(2540),
        ],
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(_("book title"), max_length=200)

    def __str__(self):
        return self.full_name
