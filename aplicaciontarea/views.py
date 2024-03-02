from django.shortcuts import render
from rest_framework import viewsets
from .models import Dulces, Electronicos, Peliculas
from .serializer import DulcesSerializer , ElectronicosSerializer,  PeliculasSerializer

# Create your views here.

class DulcesViewset(viewsets.ModelViewSet):
    queryset = Dulces.objects.all()
    serializer_class = DulcesSerializer

class ElectronicosViewset(viewsets.ModelViewSet):
    queryset = Electronicos.objects.all()
    serializer_class = ElectronicosSerializer

class PeliculasViewset(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

