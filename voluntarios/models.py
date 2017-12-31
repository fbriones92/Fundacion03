from django.db import models
from django.utils.html import format_html

class Referencia (models.Model):
    
    telefono = models.IntegerField( null = True)
    parentesco = models.CharField(max_length = 250, null = True)
    nombres = models.CharField(max_length = 250, null = True)
    apellidos = models.CharField(max_length = 250, null = True)
    
    def __str__(self):
        return self.nombres + " " + self.parentesco
    


class Voluntario(models.Model):
    SEXO_MASCULINO = 0
    SEXO_FEMENINO = 1
    SEXO_CHOICES = (
            (SEXO_MASCULINO, 'Masculino'),
            (SEXO_FEMENINO, 'Femenino'),
        )
    ESTADO_ACTIVO = 0
    ESTADO_INACTIVO = 1
    ESTADO_PASANTE = 2
    ESTADO_CHOICES = (
            (ESTADO_ACTIVO, 'Activo'),
            (ESTADO_INACTIVO, 'Inactivo'),
            (ESTADO_PASANTE, 'Pasante'),
        )
    IDIOMA_ESPANISH = 0
    IDIOMA_ENGLISH = 1
    IDIOMA_TWO = 2
    IDIOMA_CHOICES = (
            (IDIOMA_ESPANISH, 'Espanol'),
            (IDIOMA_ENGLISH, 'Ingles'),
            (IDIOMA_TWO, 'Esp-Ing'),
        )
    
    cedula = models.CharField(max_length = 10,null = True)
    nombres = models.CharField(max_length = 250, null = True)
    apellidos =  models.CharField(max_length = 250, null = True)
    edad =  models.PositiveSmallIntegerField (null = True)
    sexo = models.SmallIntegerField(choices = SEXO_CHOICES, null = True)
    fecha_nacimiento = models.DateField(null = True)
    convencional = models.CharField(max_length = 10)
    celular = models.CharField(max_length = 10, null = True)
    correo = models.EmailField(null = True)
    direccion = models.CharField(max_length = 300)
    ocupacion = models.CharField(max_length = 100)
    carrera = models.CharField(max_length = 100)
    institucion = models.CharField(max_length = 200)
    idioma = models.SmallIntegerField(choices = IDIOMA_CHOICES, null = True)
    estado = models.SmallIntegerField(choices = ESTADO_CHOICES, default = ESTADO_INACTIVO)
    referencia = models.ManyToManyField(Referencia)
    
    def __str__(self):
        return self.nombres + " " + self.apellidos
    
    