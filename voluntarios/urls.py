'''
Created on 9 dic. 2017

@author: franklin
'''
from django.conf.urls import url
from voluntarios.views import home, voluntarios, voluntario, update, ReportePersonasExcel

urlpatterns =[
     url(r'^$', home, name = "home"),
     url(r'^voluntarios/$', voluntarios, name='voluntarios'),
     url(r'^voluntarios/crear/$', voluntario, name="voluntario"),
     url(r'^voluntarios/crear/(?P<voluntario_id>\d+)$', voluntario, name="voluntario"),
     url(r'^voluntarios/deshabilitar/(?P<voluntario_id>\d+)$', update, name='update'),
     url(r'^reporte_excel/$',ReportePersonasExcel.as_view(), name="reporte_excel"),
     
       
]
