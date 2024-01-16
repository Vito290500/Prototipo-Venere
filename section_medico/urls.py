from django.urls import path
from . import views

urlpatterns = [
    path("Login/", views.LoginMedico.as_view(), name="login-medico"),
    path("Nuovo Assistito", views.NuovoAssistito, name="nuovo-assistito"),
    path("Archivio Pazienti", views.ArchivioPazienti, name="archivio-pazienti"),
    path("Calendario Prenotazioni", views.Calendario_Prenotazioni, name="calendario-prenotazioni"),
    path("Elenco Referti", views.Elenco_Referti, name="elenco-referti"),
    path("Tabella Analisi", views.Tabella_Analisi, name="tabella-analisi"),
    path("Sincronizzazione", views.Sincronizzazione, name="sincronizzazione"),
] 