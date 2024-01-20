from django.db import models

# Create your models here.
class ArchivioPazientiTest(models.Model):
    name = models.CharField(max_lenght = 100)
    cognome = models.CharField(max_lenght = 100)
    codice_fiscale = models.CharField(max_lenght = 100)
    indirizzo = models.CharField(max_lenght = 100)
    dettagli = models.CharField(max_lenght = 100)
    fine_attività = models.CharField(max_lenght = 100)
    id = models.IntegerField()