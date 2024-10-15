from django.urls import path
from inicio.views import inicio, vista_datos1, acerca_de_mi, crear_auto, buscar_auto

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('vista-datos1/<nombre>/', vista_datos1),
    path('primer-temple/', acerca_de_mi, name='acerca_de_mi'),
    path('creacion_auto_correcto/', crear_auto),
    path('buscar_auto/', buscar_auto, name='buscar_auto'),
    path('crear_auto/', crear_auto, name='crear_auto')
]