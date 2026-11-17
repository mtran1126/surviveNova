from django.shortcuts import render, redirect

def index(request):
    return render(request, "polls/index.html")


def character(request):
    if request.method == "POST":
        name = request.POST.get("character_name", "").strip()

        if name:
            request.session["character_name"] = name
            return redirect("stats")

    return render(request, "polls/character.html")


def stats(request):
    name = request.session.get("character_name")

    if not name:
        return redirect("character")

    return render(request, "polls/stats.html", {
        "name": name
    })
