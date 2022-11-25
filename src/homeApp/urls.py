from django.contrib import admin
from django.urls import path
from homeApp import views  # importing view form homeApp

urlpatterns = [
    path("", views.index, name="home"), # if koi blank path lekar ayegi to use Views k INDEX function pr bhej do, and path k name rakh do home
    path("about", views.about, name="about") , # if koi 'about' path lekar ayegi to use Views k ABOUT function pr bhej do, and path k name rakh do About
    path("services", views.services, name="services") ,
    path("contacts", views.contacts, name="contacts") ,
]
