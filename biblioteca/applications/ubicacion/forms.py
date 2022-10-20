from django import forms

class AddUbicacionForm(forms.Form):
    nombre = forms.CharField(max_length=32)
    codigo = forms.CharField(max_length=16)
    descripcion = forms.CharField(max_length=256)