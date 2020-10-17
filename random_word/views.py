from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def route(request):
    return redirect("/random_word")


def random(request):
    if "counter" in request.session:
        request.session["counter"] += 1
    else:
        request.session["counter"] = 1
    request.session['word'] = get_random_string(length=14)    
    return render(request, "index.html")


def reset(request):
    request.session.clear()
    return redirect("/random_word")
