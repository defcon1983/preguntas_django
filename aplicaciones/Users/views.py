from django.shortcuts import render

# register por medio del form en django normal
from .models import User
from django.views.generic.edit import FormView
from .forms import UserRegisterForm

# Create your views here.

#django normal
class UserCreate(FormView):
    template_name = 'users/register.html'
    success_url = '/'
    form_class = UserRegisterForm


    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            #extra fields
            pais = form.cleaned_data['pais'],
            genero = form.cleaned_data['genero'],
        )
        return super(UserCreate, self).form_valid(form)


