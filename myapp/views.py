from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#1. Módulo Público-----------------------
#a. Inicio
def inicio(request):
    return render(request,'inicio.html')
#b. Noticias
def listado_de_noticias(request):
    return render(request,'listado_de_noticias.html')
#c. Detalles de la noticia
def detalles_de_noticia(request):
    return render(request,'detalle_de_noticia.html')
#d. Cronograma
def cronograma(request):
    return render(request,'cronograma.html')
#e. Expositores
def expositores(request):
    return render(request,'expositores.html')
#2. Módulo de Asistente------------------
#a. Registro de Asistente
#b. Cuenta de usuario
#c. Impresión de Credencial
#d. Impresión de Certificado
#3. Módulo de Organizadores---------------
#a. Registro de Staff
#b. Asignación de Roles
#c. Registro de Expositores
#d. Entrega de Material
#e. Entrega de refrigerio
#f. Marcado de Asistencia
#g. Registro de Noticias


