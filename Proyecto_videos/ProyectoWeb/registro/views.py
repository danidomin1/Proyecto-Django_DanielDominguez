# views.py
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)  # Recibimos los datos del formulario
        if form.is_valid():  # Validamos que los datos sean correctos
            form.save()  # Si el formulario es válido, se guarda automáticamente en la base de datos
            return redirect('registro/registro_exitoso')  # Redirigimos a una página de éxito
    else:
        form = RegistroForm()  # Si es un GET, mostramos el formulario vacío

    return render(request, 'registro/registro.html', {'form': form})

