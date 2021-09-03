from django.db import models
from django.db.models.fields import AutoField, PositiveSmallIntegerField
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
import datetime
from .managers import RespuestasManager, PreguntasManager
# Create your models here.

class Preguntas(models.Model):
    pregunta = models.CharField('Ingresa tu pregunta', max_length=50)
    fecha_creacion = models.DateTimeField('fecha creacion', auto_now=False, auto_now_add=True)
    objects = PreguntasManager()
   
    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=200)
    preg = models.ForeignKey(Preguntas, related_name='preguntas_respuestas', on_delete=models.CASCADE)
    votos = models.IntegerField(default=0, blank=True, null=True)
    objects = RespuestasManager()


    def __str__(self):
        return self.respuesta




