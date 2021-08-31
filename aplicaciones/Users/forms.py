

from django import forms
from django.db import models
from .models import User

class UserRegisterForm(forms.ModelForm):
    # agregando los compos de password al form
    password1 = forms.CharField(
        label = 'contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña'
            }
        )
    )


    # password1 = forms.CharField(label = 'contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'contraseña'}))

    password2 = forms.CharField(
        label = 'contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'repite tu contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'pais',
            'genero',
        )



    # Validacion de los forms
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'algo salio mal checalo por')
