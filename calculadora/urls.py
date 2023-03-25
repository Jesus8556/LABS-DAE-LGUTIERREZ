from django.urls import path 
from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<str:simbolo>/<int:numero1>/<int:numero2>/", views.calculo , name="simbol"),
    
]