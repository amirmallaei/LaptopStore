from django.urls import path 
from store.views import HomeView, LaptopDetailsView,AddToCartView, CartView

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('laptop/<int:pk>/', LaptopDetailsView.as_view(), name='laptop_detail'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name="add_to_cart"),
    path('cart/', CartView.as_view(), name="cart")
]
