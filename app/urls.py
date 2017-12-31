'''
Created on 7 dic. 2017

@author: franklin
'''
from django.conf.urls import url
from app.views import website

urlpatterns =[
     url(r'^$', website, name = "website"),
    
]