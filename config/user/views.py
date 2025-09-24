from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from user.forms import UserRegisterForm
from user.models import Profile
import random
from user.tasks import send_email
# Create your views here.

class UserRegisterationView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('store:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.set_password(form.cleaned_data.get('password'))
        user.save()

        addr = form.cleaned_data.get('address')
        gender = form.cleaned_data.get('gender')
        Profile.objects.create(user=user, gender=gender, address= addr)
        otp = random.randint(100000,999999)
        send_email.delay(user.email, otp)
        return super().form_valid(form)



class LoginView(TemplateView):
    template_name = 'user/login.html'