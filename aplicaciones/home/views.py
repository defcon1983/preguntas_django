from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView

from django.views.generic.edit import (
   CreateView,
   UpdateView,
   DeleteView,
   )

from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
from .models import Preguntas, Respuesta

# practica hacerca de los filtros
def listar(request):
   """
    variaciones de filtros
   """
   data_preguntas = Preguntas.objects.all()
   # data_preguntas = Preguntas.objects.order_by('pregunta')
   # data_preguntas = Preguntas.objects.order_by('-pregunta')
   # data_preguntas = Preguntas.objects.all()[2:]
   # data_preguntas = Preguntas.objects.all()[:3]
   # data_preguntas = Preguntas.objects.filter(pregunta__startswith='a')
   # data_preguntas = Preguntas.objects.filter(edad=50)
   # data_preguntas = Preguntas.objects.filter(pregunta__contains='r')
   # data_preguntas = Preguntas.objects.filter(pregunta__icontains='e').filter(edad=5)
   # data_preguntas = Preguntas.objects.filter(pregunta__icontains='e').filter(edad=5).order_by('-pregunta')

   context = {
      'data_preguntas': data_preguntas,
   }
   return render(request, 'home/listar-datos.html', context)

"""
en la siguiente seccion se muestran las vistas de un CRUD 
completo los cuales se usaron ventanas modals para dar la
sensacion de no cambiar tanto de template
"""

# vista para listar un modelo en especifico
class PreguntasView(ListView):
   model = Preguntas
   template_name = 'home/list.html'


class PreguntasCreate(CreateView):
    model = Preguntas
    # template_name = 'home/crear.html'
    fields = [
       'pregunta'
       ]
    success_url = '/'
    # fields = '__all__'  * la sintaxis  __all__ se usa para

# esta es la clase de la vista para actualizar preguntas
class PreguntaUpdate(UpdateView):
    model = Preguntas # campo que hace referencia al modelo utilizado
    fields = ['pregunta']  # listar atributos de la tabla principal
    template_name_suffix = '_update_form'
    success_url = '/'

# logica del borrado de un objeto (pregunta)
class PreguntaDeleteView(DeleteView):
   model = Preguntas
   success_url = reverse_lazy('home:preguntas_list')

# logica del detalle de un objeto o una pregunta
class PreguntasDetailView(DetailView):
   model = Preguntas
   

"""
Esta vista basada en funcion fue usada para la parte
logica de los votos ya que podemos definir un mayor control
en la logica y peticiones de los datos al servidor
ya que en esta vista se emplearon dos modelos diferentes
los cuales estaban unidos por una clave foranea
"""

def votos(request, votos_id):
   pregunta = get_object_or_404(Preguntas, pk=votos_id)
   if request.method=='GET':
      res = Respuesta.objects.respuestas_en_preguntas(pregunta.id)
      context={
         'pregunta': pregunta,
         'res': res
      }
      return render(request, 'home/votos.html', context)
   elif request.method=='POST':
      votos = Respuesta.objects.get(pk=request.POST['votar'])
      votos.votos += 1
      votos.save()
      return HttpResponseRedirect(reverse_lazy('home:preguntas_detail', args=(pregunta.id,)))
