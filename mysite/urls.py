"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import (
    inicio, noticias, detalles_de_noticia, cronograma, expositores, registro,
    personal, sesion, ayuda, admin_qr, procesar_qr,ambientes,certificados,
    descargar_certificado
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #1. Módulo Público-----------------------
#a. Inicio
    path ('',inicio),
#b. Noticias
    path('noticias/',noticias),
#c. Detalles de la noticia
    path('detalles_de_noticia/',detalles_de_noticia),
#d. 
    path('cronograma/',cronograma),
#e. Expositores
    path('expositores/',expositores),
#2. Módulo de Asistente------------------
    path('ayuda/', ayuda), 
#a. Registro de Asistente
    path('registro/',registro),
#b. Cuenta de usuario
    path('personal/', personal),#para ver el perfil si conecta creo...
    path('sesion/', sesion),  # iniciar sesion por el momento parece que sirve

#d. Impresión de Certificado
    path('certificados/', certificados),
#g. ambientes
    path('ambientes/', ambientes),


#para que corra el qr
    path('admin_qr/', admin_qr, name='admin_qr'),
    path('procesar_qr/', procesar_qr, name='procesar_qr'),

# Ruta para descargar certificado
    path('descargar_certificado/', descargar_certificado, name='descargar_certificado'),
    
]
