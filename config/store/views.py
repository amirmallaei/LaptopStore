from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from store.models import Laptop, Cart, CartItem
# Create your views here.

class HomeView(ListView):
    template_name = 'store/index.html'
    model = Laptop


class LaptopDetailsView(DetailView):
    template_name = 'store/details.html'
    model = Laptop
    

class AddToCartView(View):
    def post(self, request, pk):
        if not self.request.user.profile.is_user():
            return redirect("user:login")
        
        laptop_item = Laptop.objects.get(id=pk)
        cart, _ = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(cart=cart, laptop=laptop_item)

        if not created:
            item.quntity +=1
            item.save()

        messages.success(request, f"{laptop_item.model_name} added to cart")
        return redirect("store:cart")
    
class CartView(TemplateView):
    template_name = "store/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user).first()
        context['cart'] = cart
        return context