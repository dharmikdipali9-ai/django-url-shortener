from django.shortcuts import render, redirect
from .models import URL

def home(request):
    short_url = None

    if request.method == "POST":
        original = request.POST.get("url")

        if original:
            obj = URL.objects.create(original_url=original)
            short_url = request.build_absolute_uri(f"/{obj.short_code}")

    return render(request, "home.html", {"short_url": short_url})


def redirect_url(request, code):
    try:
        url = URL.objects.get(short_code=code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return render(request, "404.html")