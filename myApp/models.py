from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Artista(models.Model):
    id_artista = models.IntegerField(primary_key=True)
    nom_artista = models.CharField(max_length=100)
    pais_artista = models.CharField(max_length=100)
    ruta_artista = models.CharField(max_length=100)  # Ruta a la imagen del artista
    biografia = models.TextField(null=False)  # Nueva columna de biografía
    curiosidades = models.TextField(null=True)  # Nueva columna de curiosidades

    def __str__(self):
        return self.nom_artista

    
class Epoca(models.Model):
    id_epoca = models.IntegerField(primary_key=True)
    nom_epoca = models.CharField(max_length=100)
    anyos_epoca = models.CharField(max_length=100)
    ruta_epoca = models.CharField(max_length=100) #ruta a la imagen de la epoca

    def __str__(self):
        return self.nom_epoca

class Museo(models.Model):
    id_museo = models.IntegerField(primary_key=True)
    nom_museo = models.CharField(max_length=100)
    pais_museo = models.CharField(max_length=100)
    ruta_museo = models.CharField(max_length=100) #ruta a la imagen del museo

    def __str__(self):
        return self.nom_museo

class Obras(models.Model):
    id_obra = models.IntegerField(primary_key=True)
    nom_obra = models.CharField(max_length=100)
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    id_epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE)
    id_museo = models.ForeignKey(Museo, on_delete=models.CASCADE)
    num_meGustas = models.IntegerField(default=0)
    ruta_obra = models.CharField(max_length=100)
    info = models.TextField(null=False) 

    def __str__(self):
        return self.nom_obra

class favoritas(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_obra = models.ForeignKey(Obras, on_delete=models.CASCADE)

class obrasArtista(models.Model):
    id_obra = models.ForeignKey(Obras, on_delete=models.CASCADE)
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
