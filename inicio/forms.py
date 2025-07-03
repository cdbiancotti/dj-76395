from django import forms

class FormularioBase(forms.Form):
    marca = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Fiat, Ford, Chevrolet...'
    }))
    modelo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Uno, S10, Ranger...'
    }))


class FormularioCrearAuto(FormularioBase): ...


class FormularioActualizarAuto(FormularioBase): ...

    
class FormularioBusqueda(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)
    