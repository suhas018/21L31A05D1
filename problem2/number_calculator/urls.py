# number_calculator/urls.py
from django.urls import path
from .views import get_numbers

urlpatterns = [
    path('numbers/', get_numbers, name='get_numbers'),
]
