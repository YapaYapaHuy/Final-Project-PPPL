from django.db.models.fields import CharField
from core.models import AvailableDays, CategoryChoices, ProfessionalProfile, StudentProfile, User, ConsultationRequest, Consultation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class StudentInitialForm(UserCreationForm):
    fullname = forms.CharField(required=True)
    nim = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = StudentProfile.objects.create(
            user=user,
            fullname=self.cleaned_data.get('fullname'),
            nim = self.cleaned_data.get('nim'),
            email = self.cleaned_data.get('email'))
        return user

class ProfessionalInitialForm(UserCreationForm):
    fullname = forms.CharField(required=True)
    education = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    speciality = forms.ModelMultipleChoiceField(
        queryset=CategoryChoices.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)
    available_days = forms.ModelMultipleChoiceField(
        queryset=AvailableDays.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)  

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_professional = True
        user.save()
        professional = ProfessionalProfile.objects.create(
            user=user,
            fullname = self.cleaned_data.get('fullname'),
            education = self.cleaned_data.get('education'),
            email = self.cleaned_data.get('email')
            )
        professional.speciality.add(*self.cleaned_data.get("speciality"))
        professional.available_days.add(*self.cleaned_data.get("available_days"))
        return user

class DateInput(forms.DateInput):
    input_type="date"

class ConsultationRequestForm(forms.Form):

    consultation_date = forms.DateField(widget=DateInput())
    consultation_hour = forms.CharField()
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryChoices.objects.all()
    )
    reason = forms.CharField()
    professional = forms.ModelMultipleChoiceField(
        queryset=ProfessionalProfile.objects.all()
    )
