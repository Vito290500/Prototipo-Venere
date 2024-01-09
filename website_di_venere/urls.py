from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("Medico/", include("section_medico.urls"))
]