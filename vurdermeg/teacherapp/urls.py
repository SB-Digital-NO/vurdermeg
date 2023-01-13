from django.urls import path

from .views import TeacherHome

urlpatterns = [path("", TeacherHome.as_view(), name="t_home")]
