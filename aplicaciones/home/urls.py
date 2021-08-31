

from django.conf.urls import url
from django.urls import path, re_path
from .views import (
    PreguntasView,
    PreguntasCreate,
    PreguntaUpdate,
    PreguntaDeleteView,
    PreguntasDetailView,
    listar,
    votos,
    )

app_name = 'home'

urlpatterns = [
    path('', PreguntasView.as_view(), name='preguntas_list'),
    # practica hacerca de los filtros
    path('lista/', listar, name='lista'),
    # CRUD de los modelos
    path('add/', PreguntasCreate.as_view(), name='preguntas_add'),
    path('up/<pk>', PreguntaUpdate.as_view(), name='preguntas_up'),
    path('del/<pk>', PreguntaDeleteView.as_view(), name='preguntas_del'),
    path('detail/<pk>', PreguntasDetailView.as_view(), name='preguntas_detail'),
    #los votos
    path('votos/<votos_id>', votos, name='votos'),
]


