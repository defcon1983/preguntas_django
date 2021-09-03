"""
los managers nos ayudan a distribuir la logica de una tabla o 
modelo para no sobrecargar los archivos VIEWS en los cuales 
se suele colocar todo ese codigo, y asi desde la vista o archivo
views.py solo llamaremos a la funcion que vayamos a utilizar 
en este caso seria la funcion **respuestas_en_preguntas**
y el momento de llamarla solo le pasaremos el parametro que
obtendremos de la request de forma dinamica ya sea al oprimir un
boton o en este caso un vinculo
"""

from django.db import models

class PreguntasManager(models.Manager):

    def preguntas_update(self, preguntas):

        return self.filter(
            preg__id=preguntas
        )
    """
    en el return enviamos la lista de respuestas obtenidas
    """

class RespuestasManager(models.Manager):
    """ filtrmos pormedio del ID que nos llega de la peticion
    la lista de respuestas contenidas en una pregunta por medio
    del argumento preguntas el cual contiene la ID que
    necesitamos para realizar el filtro"""

    def respuestas_en_preguntas(self, preguntas):
        return self.filter(
            preg__id=preguntas
        )