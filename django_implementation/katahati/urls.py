"""katahati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from core.views import SignUpView, StudentFormView, ProfessionalFormView, ConsultationRequestView, DashboardView, StudentRequestListView, ProfessionalRequestListView, ajax_accept_request, StudentConsultationListView, ProfessionalConsultationListView
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('accounts/signup/student/', StudentFormView.as_view(), name="student_signup"),
    path('accounts/signup/professional/', ProfessionalFormView.as_view(), name="professional_signup"),
    path('student/request/', ConsultationRequestView.as_view(), name="consultation_request"),
    path('student/request_list/', StudentRequestListView.as_view(), name="student_request_list"),
    path('student/consultation_list/', StudentConsultationListView.as_view(), name="student_consultation_list"),
    path('professional/request_list/', ProfessionalRequestListView.as_view(), name="professional_request_list"),
    path('professional/consultation_list/', ProfessionalConsultationListView.as_view(), name="professional_consultation_list"),
    path('ajax/accept_request/', ajax_accept_request, name='ajax_accept_request'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path("dashboard/", DashboardView.as_view(), name="dashboard")
]
