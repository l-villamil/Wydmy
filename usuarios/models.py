from django.db import models

class Usuario(models.Model):
    cedula=models.IntegerField(null=False,blank=False,unique=True)
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    telefono = models.IntegerField(null = False, blank = False, unique = True)
    correo = models.CharField(max_length = 50, null = False, blank = False, unique = True)
    direccion = models.CharField(max_length = 50, null = False, blank = False)


    def __str__(self):
        return '%s %s' % (self.nombre,self.cedula)