from django.urls import path 
from store.views import HomeView
urlpatterns = [
    path('', HomeView.as_view() )
]
