from django.urls import path
from user.views import UserRegisterationView, LoginView, ActivateUserView,LogoutView

app_name = "user"


urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('activate/<str:otp>/', ActivateUserView.as_view())
]
