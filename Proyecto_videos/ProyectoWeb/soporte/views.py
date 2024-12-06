from django.shortcuts import render
from django.http import HttpResponseRedirect

def soporte_view(request):
    return render(request, 'soporte/soporte.html')

def descargar_anydesk(request):
    # Redirige a la URL de descarga de AnyDesk
    return HttpResponseRedirect('https://download.anydesk.com/AnyDesk.exe')

def ir_a_sharp(request):
    # Redirige al centro de descargas de Sharp
    return HttpResponseRedirect('https://global.sharp/restricted/print/select.html?view=6')

