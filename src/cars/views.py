from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cars.models import Car
from cars.permissions import IsReceptionnist, IsMecanic, IsClient, IsMecanicCanChangeState, IsCarReceptor
from cars.serializers import CarSerializer


class CarsViewset(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # Gérer les permissions en fonction des rôles
    def get_permissions(self):
        # Création
        if self.action == 'create': # Donner l'accès à la création d'objet uniquement au recéptionniste
            permission_classes = [IsReceptionnist]
        # Modification
        elif self.action == 'update' or self.action == 'partial_update':
            if self.request.user.is_receptionnist:
                permission_classes = [IsReceptionnist, IsCarReceptor]
            elif self.request.user.is_mecanic:
                permission_classes = [IsMecanicCanChangeState]
        # Lister les données
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsReceptionnist | IsClient | IsMecanic]
        # Supprimer
        elif self.action == 'destroy':
            permission_classes = [IsReceptionnist, IsCarReceptor]
        else:
            # Pour toute autre action, l'utilisateur doit uniquement être connecté pour y accéder
            permission_classes = [IsAuthenticated]
        # Pour chaque permission dans la liste permission_classes, créé une instance avec permissions ()
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # Méthode de la classe ModelViewSet de DRF qui est appelée lors de
        # l'enregistrement d'un objet crée avec POST
        # Définir 'receptionauthor' comme l'utilisateur connecté
        serializer.save(receptionauthor=self.request.user)
