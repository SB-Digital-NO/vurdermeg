from rest_framework.serializers import ModelSerializer
from tasks.models import Choice, Question, Answer, Response, Form

"""
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'desc', 'is_complete',)
"""

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text']

class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'choices']

class FormSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'questions']

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text', 'choice']

class ResponseSerializer(ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Response
        fields = ['id', 'form', 'student', 'submitted_at', 'answers']