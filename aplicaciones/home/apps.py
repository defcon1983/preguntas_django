from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.home' 

"""
NOTA:

recuerda que en este archivo en la parte de 
name = 'aplicaciones.home' 
originalmente la ruta seria name = 'home'
pero al tener una distribucion mas clara de donde estaran nuestras
apps que vayamos contruyendo fue que nos dimos a la tarea de crear 
una carpeta llamada APLICACIONES y por eso a la ruta le agregamos
el             **aplicaciones**
"""