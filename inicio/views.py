from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Auto
from inicio.forms import CrearAutoFormulario, BuscarAutoFormulario

def inicio (request):
    #return HttpResponse('Pantalla inicio')
    return render(request, 'inicio/index.html')


def vista_datos1 (request, nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse(f'Hola {nombre_mayuscula}')

def acerca_de_mi (request):
    fecha = datetime.now()
    datos = {
        'fecha' : fecha,
        'numeros' : list(range(1, 11))
    }
    
    ''' v1
    with open(r'template\primer_template.html', 'r') as archivi_del_template:
        template = Template(archivi_del_template.read())
        
    contexto = Context(datos)
    render_template = template.render(contexto)
    '''
    
    ''' v2
    template = loader.get_template('primer_template.html')
    #contexto = Context(datos) lo hace solo el loader
    render_template = template.render(datos)
    '''
    
    #v3
    return render(request, 'inicio/acerca_de_mi.html', datos)
    
    #return HttpResponse(render_template) sirve para la version 1 y 2

    
def crear_auto(request):
        
    auto = Auto(marca='Fiat', modelo='Uno', año=2015 )
    auto.save()    
    return render (request, 'inicio/creacion_auto_correcto.html', {})

def buscar_auto(request):
    
    formulario = BuscarAutoFormulario(request.GET)
    if formulario.is_valid():
       marca = formulario.cleaned_data.get('marca')
       autos = Auto.objects.filter(marca__icontains=marca)
    else:  
        autos = Auto.objects.all()
    
    return render (request, 'inicio/buscar_auto.html', {'autos': autos, 'form': formulario})

def crear_auto(request):
    
    formulario = CrearAutoFormulario()
    
    if request.method == 'POST':
        
        '''
        auto = Auto(marca=request.POST.get('marca'), modelo=request.POST.get('modelo'), año=request.POST.get('año'))
    
        auto.save()
        '''
        
        formulario = CrearAutoFormulario(request.POST)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            auto = Auto(marca=data.get('marca'), modelo=data.get('modelo'), año=data.get('año'))
            auto.save()
            return redirect('inicio:buscar_auto')
            
    return render (request, 'inicio/crear_auto.html', {'form': formulario})