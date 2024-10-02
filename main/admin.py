from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.utils.translation import gettext_lazy as _

from main import models


@admin.register(models.User)
class UserAdmin(DjUserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "last_login",
    )
    list_display_links = ("id", "username")
    ordering = ["-id"]
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "published_at",
        "is_hardcopy_owned",
        "digital_file",
    )
    ordering = ["-id"]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    ordering = ["-id"]
