from django.shortcuts import render


def t_home(request):
    return render(request, "t_home.html")
