from django import forms

class LibroFormulario(forms.Form):
    titulo= forms.CharField(max_length=50)
    autor= forms.CharField(max_length=30)
    abstract= forms.CharField()
    

class BusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, required=False) 
    
    