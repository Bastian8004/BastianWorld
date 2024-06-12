from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('blog', views.gallery),
    path('qualifications',views.qualifications, name='qualifications'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),


]