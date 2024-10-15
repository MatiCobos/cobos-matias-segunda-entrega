from django import forms

class CrearPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    edad = forms.IntegerField()
    
class BuscarPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
