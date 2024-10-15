from django.urls import path
from inicio.views import inicio,  acerca_de_mi, crear_persona, buscar_persona

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acerca_de_mi/', acerca_de_mi, name='acerca_de_mi'),
    path('crear_persona/', crear_persona, name='crear_persona'),
    path('buscar_persona/', buscar_persona, name='buscar_persona'),
]