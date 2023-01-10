from django.shortcuts import render

# Create your views here.


def s_home(request):
    return render(request, "s_home.html")
