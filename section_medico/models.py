from django.db import models

# Create your models here.
class Prenotazioni(models.Model):
    giorno = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    nome_prenotazione = models.CharField(max_length=255)
    orario_prenotazione = models.CharField(max_length=255)

