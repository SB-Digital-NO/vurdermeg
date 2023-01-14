from baseapp.models import Assessment, AssessmentGroup, Question
from django.forms import ModelForm


class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = "__all__"


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
