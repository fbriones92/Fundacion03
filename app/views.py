from django.shortcuts import render
from django.http.response import HttpResponse
from _datetime import datetime


#ejemplo de mostror un html en la vista 
#===============================================================================
# def website (request):
#     html= """ <html><title>hola </title> <body> 
#     
#             hi five!!</body></html>"""
#     return HttpResponse(html)
#===============================================================================

 
def website(request):
    return render(request, 'app/banner.html', {
        'year':datetime.now().year,
        })
