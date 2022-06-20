"""
Función consultas del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

#nota: todas las funciones que impliquen cambios en el saldo afectarian a movimientos.

def consultar_saldo(dni):
    print(mensajes.elegir_moneda())
    moneda=input()
    saldo = funciones.obtener_saldo(dni)
    if moneda=='1':
        saldo = str(saldo) + " Pesos"
    elif moneda=='2':
        saldo=str(funciones.conversion_moneda_a_soles(saldo)) + " Soles"
    return saldo
    

def ultimos_movimientos(dni):
    """ultimos_movimientos(str)->str
    esta funcion busca en el archivo con dni.csv los ultimos 10 movimientos
    del cliente y los retorna como string
    """    
    ruta = "./movimientos_clientes/" + dni + ".csv"
    with open(ruta, "r") as movimientos:
        archivo = movimientos.readlines()
    largo = len(archivo)
    resultado = funciones.formatear_ticket("Fecha     Movimiento    Saldo    Monto"," ")
    resultado
    if largo > 10:
        largo = -10
    else:
        largo = largo * -1
    while largo < 0:
        resultado = resultado + archivo[largo]
        largo = largo + 1
    return resultado


    
def movimientos():
    #funcion que guarda los movimientos de la cuenta.
    return movimientos



        
        
                