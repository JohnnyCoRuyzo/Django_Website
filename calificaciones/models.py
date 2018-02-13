from django.db import models
from django.db.models.fields.related import ForeignKey,ManyToManyField

# Create your models here.

# ---- The Model class SubNotas, is created to contain the respective grades inside a subject calification percentage.
# ---- La clase Modelo SubNotas, es creada para contener las calificaciones respectivas dentro de un porcentaje de calificación de materia. 
class SubNotas(models.Model):
    Id = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=150)
    Porcentaje = models.PositiveIntegerField()
    Nota = models.DecimalField(max_digits=2,decimal_places=1)
    Fijar = models.BooleanField(default=False)
    def __str__(self):
        return self.Descripcion + " (" + str(self.Nota) + " - "+  str(self.Porcentaje) + "%)"
        
# ---- The Model class Notas, is created to contain the respective grades inside a subject, this grades have there own percentage.
# ---- La clase Modelo Notas, es creada para contener las calificaciones respectivas dentro de una materia, estas calificaciones 
#                             tienen su propio porcentaje.

class Notas(models.Model):
    Id = models.AutoField(primary_key=True)
    SubNotas = ManyToManyField(SubNotas, related_name="Notas", blank=True)
    Descripcion = models.CharField(max_length=150)
    Porcentaje = models.PositiveIntegerField()
    Nota = models.DecimalField(max_digits=2,decimal_places=1)
    Fijar = models.BooleanField(default=False)
    def __str__(self):
        return self.Descripcion + " (" + str(self.Nota) + " - "+  str(self.Porcentaje) + "%)"

# ---- The Model class Materias, is created to contain the respective grades inside a subject, this grades have there own percentage.
# ---- La clase Modelo Materias, 
class Materias(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=150)
    Grupo = models.PositiveSmallIntegerField(default=1)
    Creditos = models.PositiveSmallIntegerField()
    Profesor = models.CharField(max_length=150,blank=True)
    Notas = ManyToManyField(Notas, related_name="Materia", blank=True)
    def __str__(self):
        return self.Nombre + " (" + str(self.Creditos) + ")"

class Semestres(models.Model):
    Numero = models.AutoField(primary_key=True)
    Materia = ManyToManyField(Materias, related_name="Semestre")
    def __str__(self):
        return "Semestre No. " + str(self.Numero)