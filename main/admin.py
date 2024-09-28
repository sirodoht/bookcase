from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin

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
    search_fields = ("username", "email")
    ordering = ["-id"]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "published_at",
    )
    ordering = ["-id"]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
    )
    ordering = ["-id"]
