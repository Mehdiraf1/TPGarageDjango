from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {
            'receptionauthor': {'required': False}  # Exclure 'receptionauthor' des champs requis
        }