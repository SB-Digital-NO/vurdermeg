from django.urls import path

from .views import (
    AssessmentGroupsView,
    AssessmentsView,
    LoginAdmin,
    TeacherHome,
    TeacherNewAssessment,
)

urlpatterns = [
    path("", TeacherHome.as_view(), name="t_home"),
    path("newassessment/", TeacherNewAssessment.as_view(), name="t_newAssessment"),
    path("groups/", AssessmentGroupsView.as_view(), name="t_assessmentGroups"),
    path("assessments/", AssessmentsView.as_view(), name="t_assessments"),
    path("loginredirect", LoginAdmin.as_view(), name="login_admin"),
]
