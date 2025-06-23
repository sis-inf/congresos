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
from myapp.views import inicio,listado_de_noticias,detalles_de_noticia,cronograma,expositores,registro

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #1. Módulo Público-----------------------
#a. Inicio
    path ('',inicio),
#b. Noticias
    path('listado_de_noticias/',listado_de_noticias),
#c. Detalles de la noticia
    path('detalles_de_noticia/',detalles_de_noticia),
#d. 
path('cronograma/',cronograma),
#e. Expositores
path('expositores/',expositores),
#2. Módulo de Asistente------------------
#a. Registro de Asistente
path('registro/',registro),
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
    
    
]
