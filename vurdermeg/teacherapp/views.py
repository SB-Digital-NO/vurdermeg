"""Views for teacherapp."""
from datetime import datetime

from baseapp.models import Assessment, AssessmentGroup, Question
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View

from .forms import AssessmentForm, AssessmentGroupForm, QuestionFormSet


class TeacherHome(ListView):
    """View for the home page for teachers."""

    template_name = "t_home.html"
    # Content of the page

    # Content of the page
    def get_queryset(self):
        # modifies the method that retrives the queryset object used to create the SQL-statements.
        self.now = datetime.now()
        return Assessment.objects.filter(group_id__members=self.request.user)


class TeacherNewAssessment(View):
    """View for creating new assessments and new questions"""

    template_name = "t_newAssessment.html"
    # Content of the page

    # Content of the page
    def get(self, request, *args, **kwargs):
        """Method for GET request"""
        self.questions = Question.objects.filter(
            assessments__group_id__members=self.request.user
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
