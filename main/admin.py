from django.contrib import admin

from main import models


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
