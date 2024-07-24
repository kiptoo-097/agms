from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('staff/', views.staff, name='staff'),
    path('contact/', views.contact, name='contact'),
]
