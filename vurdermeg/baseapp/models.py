"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return user"""
        if not email:
            raise ValueError("User must have a valid email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Base user class"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"


class AssessmentGroup(models.Model):
    group_name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)


class Assessment(models.Model):
    name = models.CharField(max_length=150)
    group_id = models.ForeignKey(AssessmentGroup, on_delete=models.CASCADE)
    assignment_time = models.DateTimeField()
    expiry_time = models.DateTimeField()


class Question(models.Model):
    data = models.JSONField()
    assessments = models.ManyToManyField(Assessment)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()


class Tag(models.Model):
    tag_name = models.CharField(max_length=120)
    assessments = models.ManyToManyField(Assessment)
