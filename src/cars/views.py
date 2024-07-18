from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from cars.models import Car
from cars.serializers import CarSerializer


class CarsViewset(ModelViewSet):

    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()
