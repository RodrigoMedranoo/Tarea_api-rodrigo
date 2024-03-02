from django.db import models

# Create your models here.
class Dulces (models.Model):
    nombre=models.CharField(max_length= 30)
    sabor = models.CharField(max_length= 30)
    cantidad=models.IntegerField()
    creado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}--{self.creado}"
    
class Electronicos (models.Model):
    precio = models.IntegerField()
    tipo = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    creado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}--{self.creado}"
    
class Peliculas (models.Model):
    nombre = models.CharField(max_length= 30)
    Categoria = models.CharField(max_length= 30)
    Clasificacion = models.CharField(max_length= 30)
    Duracion = models.IntegerField()
    creado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}--{self.creado}"