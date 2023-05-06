from django.urls import path
from App1 import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('gasto', views.gasto, name="Gasto"),
    path('ingreso', views.ingreso, name="Ingreso"),
    path('trading', views.trading, name="Trading"),
    path('gastoFormulario', views.gastoFormulario, name="GastoFormulario"),
    path('ingresoFormulario', views.ingresoFormulario, name="IngresoFormulario"),
    path('tradingFormulario', views.tradingFormulario, name="TradingFormulario"),
    path('busquedaTrading',views.busquedaTrading,name="BusquedaTrading"), 
    path('buscar/',views.buscar),
    path('leerGastos',views.leerGastos,name='LeerGastos'),
    path('leerIngresos',views.leerIngresos,name='LeerIngresos'),
    path('leerTradings',views.leerTradings,name='LeerTradings'),
    path('eliminarGasto/<gasto_fecha>/', views.eliminarGasto, name="EliminarGasto"),
    path('eliminarIngreso/<ingreso_fecha>/', views.eliminarIngreso, name="EliminarIngreso"),
    path('eliminarTrading/<trading_fecha>/', views.eliminarTrading, name="EliminarTrading"),

]


