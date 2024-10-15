from django import forms

class CrearAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    año = forms.IntegerField()
    
class BuscarAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
