from django.shortcuts import render, redirect


def route(request):
    return redirect("/random_word")


def random(request):
    request.session["counter"] = 1
    return render(request, "index.html")
