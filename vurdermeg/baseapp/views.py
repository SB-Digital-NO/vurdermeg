from django.shortcuts import render


def login(request):
    return render(request, "baseapp/login.html")
