'''
Created on 3 dic. 2017

@author: franklin
'''

from django.forms import ModelForm
from django import forms
#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _
from voluntarios.models import Voluntario, Referencia
from django.forms.fields import DateField
from django.forms.widgets import Select, NumberInput, TextInput, DateInput
#from numbers import Number
#from django.forms.fields import CharField#


class VoluntarioForm(ModelForm):
    class Meta:
        model = Voluntario
        fields = ['cedula', 'nombres', 'apellidos', 'edad','sexo',
                  'fecha_nacimiento','convencional','celular','correo',
                  'direccion','ocupacion','carrera','institucion', 'idioma', 'referencia']
        widgets= {
            'convencional': NumberInput(),
            'celular': NumberInput(),
            #===================================================================
            # 'carrera': TextInput(),
            # 'ocupacion': TextInput(),
            # 'institucion': TextInput(),
            #===================================================================
            }
        
        
class ReferenciaForm(ModelForm):
    class Meta:
        model = Referencia
        fields = '__all__'        