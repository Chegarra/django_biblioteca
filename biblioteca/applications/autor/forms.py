from django import forms
from .models import Autor

class AutorCreateForm(forms.ModelForm):
    
    class Meta:
        model = Autor
        fields = (
            'nombre',
            'apellidos',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese el nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese los apellidos'
                }
            )
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        nombre = nombre.strip()
        if len(nombre) <= 0:
            raise forms.ValidationError('Nombre en blanco')

        return nombre
