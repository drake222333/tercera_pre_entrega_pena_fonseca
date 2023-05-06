from django.shortcuts import render
from App1.models import *  #Gasto, Ingreso, Trading
from django.http import HttpResponse
from App1.forms import * #GastoFormulario, IngresoFormulario, TradingFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def gasto(request):
    return render(request,'App1/gastos.html')
def ingreso(request):
    return render(request,'App1/ingresos.html')
def trading(request):
    return render(request,'App1/tradings.html')

###gastos POST
def gasto(request):  ######depronto agregar eses ssss a estas funciones
    if request.method =='POST':
        miFormulario=GastoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            gasto=Gasto(int(informacion['id']),str(informacion['fecha']),int(informacion['renta']),
                        int(informacion['alimentacion']),int(informacion['educacion']),
                        int(informacion['transporte']),int(informacion['bills']),
                        int(informacion['vestuario']),int(informacion['recreacion']),
                        int(informacion['otros']))
            gasto.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=GastoFormulario()
    return render(request, 'App1/gastos.html', {"miFormulario": miFormulario})

###ingreso POST
def ingreso(request):
    if request.method =='POST':
        miFormulario=IngresoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            ingreso=Ingreso(int(informacion['id']),str(informacion['fecha']),int(informacion['salario']),
                            int(informacion['part_time']),int(informacion['alquileres']),
                            int(informacion['otros']))
            ingreso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=IngresoFormulario()
    return render(request, 'App1/ingresos.html', {"miFormulario": miFormulario})

###trading POST
def trading(request):
    if request.method =='POST':
        miFormulario=TradingFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            trading=Trading(int(informacion['id']),str(informacion['fecha']),
                            int(informacion['cryptocurrency']),int(informacion['acciones']),
                            int(informacion['otros']))
            trading.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=TradingFormulario()
    return render(request, 'App1/tradings.html', {"miFormulario": miFormulario})

###TRADINGFORMULARIO
def gastoFormulario(request):
     if request.method == "POST":
        miFormulario = GastoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            gasto = Gasto(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['renta']),int(informacion['alimentacion']), 
                              int(informacion['educacion']),int(informacion['transporte']),
                              int(informacion['bills']),int(informacion['vestuario']),
                              int(informacion['recreacion']),int(informacion['otros']))
            gasto.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = GastoFormulario()
             
     return render(request, "App1/gastoFormulario.html", {"miFormulario": miFormulario})
###
def ingresoFormulario(request):
     if request.method == "POST":
        miFormulario = IngresoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            ingreso = Ingreso(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['salario']),int(informacion['part_time']), 
                              int(informacion['alquileres']),int(informacion['otros']))
            ingreso.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = IngresoFormulario()
             
     return render(request, "App1/ingresoFormulario.html", {"miFormulario": miFormulario})
###
def tradingFormulario(request):
     if request.method == "POST":
        miFormulario = TradingFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            trading = Trading(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['cryptocurrency']),int(informacion['acciones']), 
                              int(informacion['otros']))
            trading.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = TradingFormulario()
             
     return render(request, "App1/tradingFormulario.html", {"miFormulario": miFormulario})

###busqueda REQUEST
def busquedaTrading(request):
     return render(request,'App1/inicio.html')

def buscar(request):
     if request.GET['fecha']:
          fecha = request.GET['fecha']
          fechas= Trading.objects.filter(fecha__icontains=fecha)

          return render(request,'App1/inicio.html', {"fechas":fechas, "comisiones": fechas })
     else:
          respuesta= "No enviaste datos"
    

     return HttpResponse(respuesta)
        
###leer REQUEST
def leerGastos(request):
    gastos= Gasto.objects.all() # trae a todos los gastos
    contexto= {"gastos": gastos}
    return render(request, "App1/leerGastos.html",contexto)

def leerIngresos(request):
    ingresos= Ingreso.objects.all() # trae a todos los ingresos
    contexto= {"ingresos": ingresos}
    return render(request, "App1/leerIngresos.html",contexto)

def leerTradings(request):
    tradings= Trading.objects.all() # trae a todos los tradings
    contexto= {"tradings": tradings}
    return render(request, "App1/leerTradings.html",contexto)

###delete
def eliminarGasto(request, gasto_fecha):
    gasto = Gasto.objects.get(fecha=gasto_fecha)
    gasto.delete()
    # vuelvo al menú
    gastos = Gasto.objects.all()  # trae todos los gastos 
    contexto = {"gastos": gastos}
    return render(request, "App1/leerGastos.html", contexto)

def eliminarIngreso(request, ingreso_fecha):
    ingreso = Ingreso.objects.get(fecha=ingreso_fecha)
    ingreso.delete()
    # vuelvo al menú
    ingresos = Ingreso.objects.all()  # trae todos los ingresos
    contexto = {"ingresos": ingresos}
    return render(request, "App1/leerIngresos.html", contexto)

def eliminarTrading(request, trading_fecha):
    trading = Trading.objects.get(fecha=trading_fecha)
    trading.delete()
    # vuelvo al menú
    tradings = Trading.objects.all()  # trae todos los tradings
    contexto = {"tradings": tradings}
    return render(request, "App1/leerTradings.html", contexto)


