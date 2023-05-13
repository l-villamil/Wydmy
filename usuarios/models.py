from django.db import models

class Usuario(models.Model):
    cedula=models.IntegerField(null=False,blank=False,unique=False)
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    telefono = models.IntegerField(null = False, blank = False, unique = False)
    correo = models.CharField(max_length = 50, null = False, blank = False, unique = False)
    direccion = models.CharField(max_length = 50, null = False, blank = False)


    def __str__(self):
        return '%s %s' % (self.nombre,self.cedula)