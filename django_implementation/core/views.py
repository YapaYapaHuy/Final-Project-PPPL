from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

from .forms import StudentInitialForm, ProfessionalInitialForm, ConsultationRequestForm
from .models import CategoryChoices, StudentProfile, ProfessionalProfile, Consultation, ConsultationRequest, User

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

@method_decorator([login_required], name='dispatch')
class DashboardView(View):
    model = User

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_student:
            return redirect("core:student_dashboard")
        elif request.user.is_professional:
            return redirect("core:professional_dashboard")
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

class SignUpView(TemplateView):
    template_name = 'account/signup.html'

class HomeView(TemplateView):
    template_name = "home.html"

class StudentDashboardView(TemplateView):
    template_name = "student_dashboard.html"

class ProfessionalDashboardView(TemplateView):
    template_name = "professional_dashboard.html"

class StudentFormView(CreateView):
    model = User
    form_class = StudentInitialForm
    template_name = "account/signup_form.html"
    
    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("core:student_dashboard")

class ProfessionalFormView(CreateView):
    model = User
    form_class = ProfessionalInitialForm
    template_name = "account/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "professional"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("core:professional_dashboard")

class ConsultationRequestView(View):
    
    def get(self, *args, **kwargs):
        form = ConsultationRequestForm()
        context = {
            'form' : form,
            "object_list" : ProfessionalProfile.objects.all()
        }
        return render(self.request, "request_form.html", context)

    def post(self, *args, **kwargs):
        form = ConsultationRequestForm(self.request.POST or None)
        if form.is_valid():
            consultation_date = form.cleaned_data.get("consultation_date")
            consultation_hour = form.cleaned_data.get("consultation_hour")
            category = form.cleaned_data.get("category")[0]
            reason = form.cleaned_data.get("reason")
            professional = form.cleaned_data.get("professional")[0]

            request = ConsultationRequest(
                # user = self.request.user,
                consultation_date = consultation_date,
                consultation_hour = consultation_hour,
                reason = reason,
            )
            request.save()
            category_obj = CategoryChoices.objects.filter(category=category).values_list("id", flat=True)
            request.category.add(category_obj[0])
            request.professional = ProfessionalProfile.objects.filter(user=professional)[0]
            request.student = StudentProfile.objects.filter(user=self.request.user)[0]
            request.save()
        return redirect("dashboard")

class StudentRequestListView(ListView):
    model = ConsultationRequest
    paginate_by = 10
    template_name = "student_request_list.html"

    def get_queryset(self):
        filter_val = StudentProfile.objects.filter(user=self.request.user)[0]
        new_context = ConsultationRequest.objects.filter(
            student=filter_val,
        )
        return new_context

class ProfessionalRequestListView(ListView):
    model = ConsultationRequest
    paginate_by = 10
    template_name = "professional_request_list.html"

    def get_queryset(self):
        filter_val = self.request.user
        new_context = ConsultationRequest.objects.filter(
            professional__user=filter_val,
        )
        return new_context

def ajax_accept_request(request):
    request_id = request.GET.get('request_id')
    consul_request = ConsultationRequest.objects.get(pk=request_id)
    try:
        consul_request.accepted = True
        consul_request.save()
        
        new_consultation = Consultation(
            request = consul_request,
            student = consul_request.student,
            professional = consul_request.professional
            )
        new_consultation.save()

        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})

class StudentConsultationListView(ListView):
    model = Consultation
    paginate_by = 10
    template_name = "student_consultation_list.html"

    def get_queryset(self):
        filter_val = StudentProfile.objects.filter(user=self.request.user)[0]
        new_context = Consultation.objects.filter(
            student=filter_val,
        )
        return new_context

class ProfessionalConsultationListView(ListView):
    model = Consultation
    paginate_by = 10
    template_name = "professional_consultation_list.html"

    def get_queryset(self):
        filter_val = ProfessionalProfile.objects.filter(user=self.request.user)[0]
        new_context = Consultation.objects.filter(
            professional=filter_val,
        )
        return new_context