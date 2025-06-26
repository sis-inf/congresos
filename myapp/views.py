from django.shortcuts import render, redirect
from .models import Asistente
from .forms import RegistroForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa

def inicio(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, 'noticias.html')

def detalles_de_noticia(request):
    return render(request, 'detalle_de_noticia.html')

def cronograma(request):
    return render(request, 'cronograma.html')

def expositores(request):
    return render(request, 'expositores.html')

def ambientes(request):
    return render(request, 'ambiente.html')
def certificados(request):
    return render(request, 'certificados.html')

def personal(request):
    correo = request.session.get('correo')
    asistente = None
    if correo:
        try:
            asistente = Asistente.objects.get(correo=correo)
        except Asistente.DoesNotExist:
            asistente = None
    return render(request, 'personal.html', {'asistente': asistente})

def sesion(request):
    mensaje = ""
    if request.method == "POST":
        correo = request.POST.get("usuario")
        contrasena = request.POST.get("contrasena")
        try:
            asistente = Asistente.objects.get(correo=correo, contrasena=contrasena)
            request.session['correo'] = asistente.correo
            return redirect('/')
        except Asistente.DoesNotExist:
            mensaje = "Correo o contraseña incorrectos"
    return render(request, 'sesion.html', {"mensaje": mensaje})

def ayuda(request):
    return render(request, 'ayuda.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            Asistente.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                ci=form.cleaned_data['ci'],
                correo=form.cleaned_data['correo'],
                contrasena=form.cleaned_data['contrasena']
            )
            return render(request, 'registro.html', {'form': RegistroForm(), 'mensaje': '¡Registro exitoso!'})
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
## para correr el los cochinos qrs
def admin_qr(request):
    return render(request, 'admin_qr.html')

@csrf_exempt
def procesar_qr(request):
    if request.method == "POST":
        data = json.loads(request.body)
        qr = data.get('qr', '')
        if qr.startswith('asistencia-'):
            id_asistente = qr.replace('asistencia-', '')
            try:
                asistente = Asistente.objects.get(id=id_asistente)
                if not hasattr(asistente, 'puntos_asistencia'):
                    asistente.puntos_asistencia = 0
                asistente.puntos_asistencia += 1
                asistente.save()
                return JsonResponse({'mensaje': '¡Asistencia registrada!'})
            except Asistente.DoesNotExist:
                return JsonResponse({'mensaje': 'Usuario no encontrado'})
        elif qr.startswith('comida-'):
            id_asistente = qr.replace('comida-', '')
            try:
                asistente = Asistente.objects.get(id=id_asistente)
                if not hasattr(asistente, 'puntos_comida'):
                    asistente.puntos_comida = 0
                asistente.puntos_comida += 1
                asistente.save()
                return JsonResponse({'mensaje': '¡Comida registrada!'})
            except Asistente.DoesNotExist:
                return JsonResponse({'mensaje': 'Usuario no encontrado'})
        else:
            return JsonResponse({'mensaje': 'QR no válido'})
    return JsonResponse({'mensaje': 'Método no permitido'})

def descargar_certificado(request):
    correo = request.session.get('correo')
    if not correo:
        return redirect('sesion')
    try:
        asistente = Asistente.objects.get(correo=correo)
    except Asistente.DoesNotExist:
        return redirect('sesion')
    if asistente.puntos_asistencia < 20:
        return HttpResponse("Necesitas al menos 20 puntos de asistencia para descargar tu certificado.", status=403)
    html = render_to_string('certificado_pdf.html', {'asistente': asistente})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado_congreso.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

