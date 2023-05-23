from django.db import models

# Create your models here.

class Coleta(models.Model):
    preferencias = {}
    preferencias['categoria'] = 'teste categoria'
    preferencias['ingrediente'] = 'teste ingrediente'
    
