"""Views for teacherapp."""
import os
from datetime import datetime

from baseapp.models import Assessment, AssessmentGroup, Question
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.base import View
from dotenv import load_dotenv

from .forms import AssessmentForm, AssessmentGroupForm, QuestionFormSet

# --== ONLY FOR DEVELOPMENT - REMOVE ON DEPLYMENT ==--
load_dotenv()
ADMIN_LOGIN = os.getenv("PW")
ADMIN_USER = os.getenv("ADMIN_USER")


class LoginAdmin(View):
    def get(self, request, *args, **kwargs):
        user = authenticate(username=ADMIN_USER, password=ADMIN_LOGIN)
        if user is not None:
            login(request, user)
            return redirect("t_home")


# --== -------------------- == --


class TeacherHome(ListView):
    """View for the home page for teachers."""

    template_name = "t_home.html"

    def get_queryset(self):
        # modifies the method that retrives the queryset object used to create the SQL-statements.
        self.now = timezone.now()  # <------ For use later when adding date filtering.
        return Assessment.objects.filter(group__members=self.request.user)

    def get_context_data(self, **kwargs):
        # Method called to get the context of the html response
        # Use this to set page content
        context = super(TeacherHome, self).get_context_data(
            **kwargs
        )  # get the context of the ListView parent class
        assessments = []
        for assessment in context["object_list"].values():
            dateTimeObj: datetime = assessment["assignment_time"]
            ass_dict = {
                "is_assigned": dateTimeObj <= self.now,
                "assignment_day": dateTimeObj.strftime("%a"),
                "assignment_date": dateTimeObj.strftime("%d"),
                "assignmet_week": dateTimeObj.strftime("%W"),
                "assignment_time": dateTimeObj.strftime("%H:%M"),
                "assignment_month": dateTimeObj.strftime("%b"),
                "name": assessment["name"],
                "group": context["object_list"].get(id=assessment["id"]).group.name,
                "expiry_time": assessment["expiry_time"],
            }
            assessments.append(ass_dict)
        context["assessments"] = assessments  # Use this to access data in template
        context["new_assessment_text"] = "Ny egenvurdering"
        return context


class TeacherNewAssessment(View):
    """View for creating new assessments and new questions"""

    template_name = "t_newAssessment.html"
    # Content of the page

    # Content of the page
    def get(self, request, *args, **kwargs):
        """Method for GET request"""
        self.questions = Question.objects.filter(
            assessments__group__members=self.request.user
        )
        self.assessment_form = AssessmentForm(request.GET or None)
        self.question_formset = QuestionFormSet()
        self.ctxt = {
            "assessment_form": self.assessment_form,
            "question_forms": self.question_formset,
            "questions": self.questions,
        }
        return render(request, self.template_name, self.ctxt)

    def post(self, request, *args, **kwargs):
        """Method for POST request"""
        self.assessment_form = AssessmentForm(request.POST or None)
        self.question_formset = QuestionFormSet(request.POST or None)
        if self.question_formset.is_valid() and self.assessment_form.is_valid():
            self.assessment = self.assessment_form.save()
            for form in self.question_formset:
                self.question = form.save()
                # Add assessment PrivateKey to the ManyToMany field "assessments" after saving the form.
                self.question.assessments.add(self.assessment.pk)
                self.question.save()
            return redirect("t_home")
        return render(
            request,
            self.template_name,
            {
                "assessment_form": self.assessment_form,
                "question_forms": self.question_formset,
            },
        )


class AssessmentGroupsView(View):
    """View for viewing and creating assessment groups."""

    template_name = "t_assessmentGroups.html"

    def get(self, request, *args, **kwargs):
        """Method for GET request"""
        self.assessment_groups = AssessmentGroup.objects.filter(members=request.user)
        self.assessment_group_form = AssessmentGroupForm(request.GET or None)
        return render(
            request,
            self.template_name,
            {
                "assessment_groups": self.assessment_groups,
                "assessment_group_form": self.assessment_group_form,
            },
        )

    def post(self, request, *args, **kwargs):
        """Method for POST request"""
        self.assessment_groups = AssessmentGroup.objects.filter(members=request.user)
        self.assessment_group_form = AssessmentGroupForm(request.POST or None)

        if self.assessment_group_form.is_valid():
            self.assessment_group_form.save()
            return redirect("t_assessmentGroups")
        return render(
            request,
            self.template_name,
            {
                "assessment_groups": self.assessment_groups,
                "assessment_group_form": self.assessment_group_form,
            },
        )


class AssessmentsView(ListView):
    """View for teachers assessments page."""

    template_name = "t_assessments.html"

    def get_queryset(self):
        return Assessment.objects.filter(group__members=self.request.user)
