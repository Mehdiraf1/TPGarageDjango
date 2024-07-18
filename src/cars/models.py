from django.db import models


class Car(models.Model):
    immatriculation = models.CharField()
    marque = models.CharField()
    modele = models.CharField()
    etat = models.CharField()

