from django.contrib import admin

from .models import StudentProfile, ProfessionalProfile, CategoryChoices, AvailableDays, ConsultationRequest, Consultation

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(ProfessionalProfile)
admin.site.register(CategoryChoices)
admin.site.register(AvailableDays)
admin.site.register(ConsultationRequest)
admin.site.register(Consultation)