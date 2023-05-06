from django import forms
 
class GastoFormulario(forms.Form):
    id= forms.IntegerField() 
    fecha= forms.DateField() 
    renta= forms.IntegerField()
    alimentacion= forms.IntegerField()
    educacion= forms.IntegerField()
    transporte= forms.IntegerField()    
    bills= forms.IntegerField()
    vestuario= forms.IntegerField()
    recreacion= forms.IntegerField()  
    otros= forms.IntegerField()

class IngresoFormulario(forms.Form):
    id= forms.IntegerField()
    fecha= forms.DateField()
    salario= forms.IntegerField()
    part_time= forms.IntegerField()
    alquileres= forms.IntegerField()    
    otros= forms.IntegerField() 

class TradingFormulario(forms.Form):
    id= forms.IntegerField()
    fecha= forms.DateField()
    cryptocurrency= forms.IntegerField()
    acciones= forms.IntegerField()
    otros= forms.IntegerField()

