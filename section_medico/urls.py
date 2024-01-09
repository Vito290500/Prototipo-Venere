from django.urls import path
from . import views

urlpatterns = [
    path("Login/", views.LoginMedico.as_view(), name="login-medico"),
]