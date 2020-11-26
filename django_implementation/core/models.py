from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

# CATEGORY_CHOICES = (
#     ("MD", "Mood Disorder"),
#     ("A", "Anxiety"),
#     ("PD", "Personality Disorder"),
#     ("ED", "Eating Disorder"),
#     ("T", "Trauma"),
#     ("SA", "Substance Abuse")
# )

# AVAILABLE_DAYS = (
#     ("M", "Monday"),
#     ("Tu", "Tuesday"),
#     ("W", "Wednesday"),
#     ("Th", "Thursday"),
#     ("F", "Friday"),
#     ("Sa", "Saturday"),
#     ("Su", "Sunday")
# )

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.TextField(default="NAME")
    nim = models.TextField()
    email = models.EmailField(default="EMAIL")

    def __str__(self):
        return self.user.username

class CategoryChoices(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class AvailableDays(models.Model):
    days = models.CharField( max_length=20)

    def __str__(self):
        return self.days

class ProfessionalProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.TextField(null=True)
    email = models.EmailField(null=True)
    education = models.TextField()
    speciality = models.ManyToManyField(CategoryChoices)
    available_days = models.ManyToManyField(AvailableDays)

    def __str__(self):
        return self.user.username

class ConsultationRequest(models.Model):
    # user = models.ForeignKey(
    #     "User", on_delete=models.CASCADE
    # )
    student = models.ForeignKey(
        "StudentProfile",  on_delete=models.SET_NULL, blank=True, null=True
    )
    professional = models.ForeignKey(
        "ProfessionalProfile",  on_delete=models.SET_NULL, blank=True, null=True
    )
    accepted = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)
    consultation_date = models.DateField(null=True)
    consultation_hour = models.CharField(null=True, max_length=20)
    category = models.ManyToManyField(CategoryChoices)
    reason = models.TextField()
    
    def __str__(self):
        return self.student.user.username

class Consultation(models.Model):
    request = models.ForeignKey(
        "ConsultationRequest", related_name="request", on_delete=models.SET_NULL, blank=True, null=True
    )
    student = models.ForeignKey(
        "StudentProfile", related_name="student", on_delete=models.SET_NULL, blank=True, null=True
    )
    professional = models.ForeignKey(
        "ProfessionalProfile", related_name="professional", on_delete=models.SET_NULL, blank=True, null=True
    )
    gmeet_link = models.TextField(null=True)

    def __str__(self):
        return f"{self.pk}"