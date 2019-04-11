from django import forms
from asociados.models import Asociado

class AsociadoForm(forms.ModelForm):
    OPTIONS = (("Soltero(a)","Soltero(a)"), ("Casado(a)","Casado(a)"), ("Otro","Otro"))

    estado_civil=forms.ChoiceField(choices=OPTIONS)
    class Meta:
        model=Asociado
        fields=[
            'nombre',
            'apellido',
            'estado_civil',
            'telefono',
            'profesion',
            'trabajo',
            'direccion'
        ]
        labels = {
            'nombrec': 'Nombre',
            'apellido': 'Apellido',
            'estado_civil':'Estado Civil',
            'telefono':'Teléfono',
            'profesion':'Profesión',
            'direccion':'Dirección'

        }



