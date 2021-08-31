from django.contrib import admin

# Register your models here.
from .models import Preguntas, Respuesta

"""
los ModelAdmin nos ayudan a personalizar nuestro administrador 
a la medida de lo posible iremos viendo mas cosas que podemos
ir agregando
"""

class Preg(admin.ModelAdmin):
    # nos da un listado de los campos que le indiquemos
    list_display = (
        'pregunta',
        
    )
    # nos activa un buscador con los campos que le indiquemos
    search_fields = (
        'pregunta',
    )
    """
    nos activa unos filtros que considero que se ven mejor 
    cuando estamos usando compos del tipo booleanfields 
    (True o False
    """
    list_filter = (
        'pregunta',
    )

"""
por ultimo esa clase del ModelAdmin hay que registrarla 
junto al modelo para que los cambios surtan efecto
"""
admin.site.register(Preguntas, Preg)




admin.site.register(Respuesta)
