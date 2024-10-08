from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(_("username"), max_length=100, unique=True)
    email = models.EmailField(_("email"), unique=True)


class Author(models.Model):
    name = models.CharField(_("author full name"), max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_("book title"), max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_hardcopy_owned = models.BooleanField(default=False)
    digital_file = models.FileField(null=True)
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
