from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase

from cars.models import Car


class TestCar(APITestCase):

    url = reverse_lazy('cars-list')

    # Test de GET
    def test_list(self):
        # Création d'un objet
        car = Car.objects.create(
            immatriculation='GF-642-TT',
            marque='Renault',
            modele='Clio',
            etat='En cours'
        )

        # Stockage des données attendues en JSON
        dataexpected = [
            {
                'immatriculation': car.immatriculation,
                'marque': car.marque,
                'modele': car.modele,
                'etat': car.etat,
            }
        ]

        response = self.client.get(self.url)
        # Vérifier que l'URL marche et qu'il n'y'a pas d'erreur
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), dataexpected)

    # Test de POST
    def test_create(self):

        # Vérifier que la BD est vide
        self.assertEqual(Car.objects.count(), 0)

        # Tester la création d'un nouvel objet
        response = self.client.post(self.url, data={
            'immatriculation': 'GF-642-TT',
            'marque': 'Renault',
            'modele': 'Clio',
            'etat': 'En cours'
        })
        self.assertEqual(response.status_code, 201)

        # Vérifier si l'objet a été enregistrer dans la BD
        self.assertEqual(Car.objects.count(), 1)

    # Test de UPDATE
    def test_update(self):

        car = Car.objects.create(
            immatriculation='GF-642-TT',
            marque='Renault',
            modele='Clio',
            etat='En cours'
        )

        self.client.put(reverse('cars-detail', kwargs={'pk': car.pk}), data={
            'immatriculation': 'GF-642-TT',
            'marque': 'Renault',
            'modele': 'Clio',
            'etat': 'Fini'
        })

        # Actualiser les attributs de car depuis la BD
        car.refresh_from_db()
        self.assertEqual(car.etat, 'Fini')

    def test_delete(self):

        # On vérifie que la BD est vide
        car_count = Car.objects.count()
        self.assertEqual(car_count, 0)

        # On crée un objet car
        car = Car.objects.create(
            immatriculation='GF-642-TT',
            marque='Renault',
            modele='Clio',
            etat='En cours'
        )

        # On crée un objet car
        car_count = Car.objects.count()
        self.assertEqual(car_count, 1)

        self.client.delete(reverse('cars-detail', kwargs={'pk': car.pk}))

        car_count = Car.objects.count()
        self.assertEqual(car_count, 0)
