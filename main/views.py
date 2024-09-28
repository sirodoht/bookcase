from django.shortcuts import render

from main import models


def index(request):
    return render(
        request,
        "main/index.html",
        {"book_list": models.Book.objects.all()},
    )
