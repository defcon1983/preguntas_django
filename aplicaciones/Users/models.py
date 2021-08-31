



from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    add_choice = [
        ('0', 'chile'),
        ('1', 'mexico'),
        ('2', 'salvador'),
        ('3', 'peru'),
    ]

    genero = [
        ('m', 'mujer'),
        ('h', 'hombre'),
    ]
    email = models.EmailField('Email Address', max_length=254, unique=True)
    username = models.CharField('usuario', max_length=50, unique=True)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    objects = UserManager()
    pais = models.CharField('pais', max_length=1, choices= add_choice)
    genero = models.CharField('genero', max_length=1, choices= genero)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

