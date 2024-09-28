from django.urls import path
from . import views

app_name = "Contacto"

urlpatterns = [
    path("",views.Contacto,name="contacto"),
]    