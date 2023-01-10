from django.shortcuts import render


def teacherhome(request):
    return render(request, "teacherhome.html")
