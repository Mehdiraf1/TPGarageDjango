from django.contrib.auth.models import AbstractUser, User
from django.db import models

from ProjectGarage import settings


class Car(models.Model):
    immatriculation = models.CharField(max_length=100, primary_key=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    etat = models.CharField(max_length=100)

    receptionauthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.immatriculation


class CustomUser(AbstractUser):

    is_receptionnist = models.BooleanField(default=False)
    is_mecanic = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


