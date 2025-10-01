from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from store.models import Laptop
# Create your views here.

class HomeView(ListView):
    template_name = 'store/index.html'
    model = Laptop


class LaptopDetailsView(DetailView):
    template_name = 'store/details.html'
    model = Laptop
    