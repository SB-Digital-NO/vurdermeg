from helpers.models import TrackingModel
from django.db import models
from authentication.models import User

class Class(TrackingModel):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, related_name='classes', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='student_classes')

class Form(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='forms')

class Question(TrackingModel):
    text = models.CharField(max_length=1024)
    type = models.CharField(max_length=255)  # E.g., 'rating', 'multiple_choice', 'open_ended'
    form = models.ForeignKey(Form, related_name='questions', on_delete=models.CASCADE)

class Choice(TrackingModel):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

class Response(TrackingModel):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Answer(TrackingModel):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True)  # For open-ended
    choice = models.ManyToManyField(Choice, blank=True)  # For multiple choice

"""
class Task(TrackingModel):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
"""