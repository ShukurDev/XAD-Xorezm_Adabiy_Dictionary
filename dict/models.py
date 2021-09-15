from django.db import models

# Create your models here.

class Lugat(models.Model):
    adabiy = models.CharField('Adabiy (soz)' , max_length=100)
    xorazmcha = models.CharField('Xorazm (soz)' ,max_length=100)

