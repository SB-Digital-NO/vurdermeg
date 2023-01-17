from django.urls import path

from .views import TeacherHome, TeacherNewAssessment

urlpatterns = [
    path("", TeacherHome.as_view(), name="t_home"),
    path("newassessment/", TeacherNewAssessment.as_view(), name="t_newAssessment"),
]
