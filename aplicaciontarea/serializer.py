from rest_framework import serializers
from .models import Dulces, Electronicos, Peliculas

class DulcesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dulces
        fields='__all__'

class ElectronicosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Electronicos
        fields='__all__'

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Peliculas
        fields='__all__'