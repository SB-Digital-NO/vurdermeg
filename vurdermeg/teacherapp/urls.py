from django.urls import path

from . import views

urlpatterns = [path("", views.t_home, name="t_home")]
