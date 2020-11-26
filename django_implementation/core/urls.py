from django.urls import path, include

from .views import (
    HomeView,
    StudentFormView,
    ProfessionalFormView,
    StudentDashboardView,
    ProfessionalDashboardView,
    ConsultationRequestView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/student/', StudentDashboardView.as_view(), name="student_dashboard"),
    path('dashboard/professional/', ProfessionalDashboardView.as_view(), name="professional_dashboard"),
]   