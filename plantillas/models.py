from django.db import models

class Plantilla(models.Model):
    nombre=models.CharField(max_length = 50, null = False, blank = False)
    medico=models.CharField(max_length = 50, null = False, blank = False)
    procedimiento=models.CharField(max_length = 50, null = False, blank = False)
    hospital=models.CharField(max_length = 50, null = False, blank = False)


    def __str__(self):
        return '%s %s' % (self.nombre,self.medico)