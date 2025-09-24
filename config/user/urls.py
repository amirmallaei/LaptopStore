from django.urls import path
from user.views import UserRegisterationView, LoginView

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login")
]
