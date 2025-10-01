from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from user.forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from user.models import Profile
import random
from user.tasks import send_email
from django.conf import settings
from django.contrib.auth import get_user_model

USER = get_user_model() 
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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("store:home")

class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('store:home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(username=email, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid email or password")
            return self.form_invalid(form)


class ActivateUserView(View):
    def get(self, request, otp):
        email_bytes = settings.REDIS_INSTANCE.get(f"{otp}")
        if email_bytes:
            email = email_bytes.decode('utf-8')
            user= USER.objects.get(email=email)
            user.is_active = True
            user.save()
            settings.REDIS_INSTANCE.delete(f"{otp}")
            return redirect("store:home")
