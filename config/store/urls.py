from django.urls import path 
from store.views import HomeView, LaptopDetailsView

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('laptop/<int:pk>/', LaptopDetailsView.as_view(), name='laptop_detail'),
]
