from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Persona
from inicio.forms import CrearPersonaFormulario, BuscarPersonaFormulario

def inicio (request):

    return render(request, 'inicio/index.html')


def acerca_de_mi (request):

    return render(request, 'inicio/acerca_de_mi.html')

def crear_persona(request):
    formulario = CrearPersonaFormulario()

    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            persona = Persona(nombre=data.get('nombre'), apellido=data.get('apellido'), edad=data.get('edad'))
            persona.save()
            return redirect('inicio:buscar_persona')

    return render(request, 'inicio/crear_persona.html', {'form': formulario})

def buscar_persona(request):
    formulario = BuscarPersonaFormulario(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()

    return render(request, 'inicio/buscar_persona.html', {'personas': personas, 'form': formulario})