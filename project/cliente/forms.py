from django import forms
from . import  models

class clienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre","apellido","nacimiento","pais_origen_id"]

