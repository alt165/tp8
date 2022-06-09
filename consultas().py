"""
Función consultas del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""

from import

#nota: todas las funciones que impliquen cambios en el saldo afectarian a movimientos.

def saldo():
    #esta funcion guardaria los saldos, y una vez que se invoca una extracion deberia cambiar.
    return saldo

def saldo_disponible(saldo):
    if moneda==2:
        saldo_disponible=conversion_moneda_a_soles(saldo)
    else:
        saldo_disponible=saldo
    print('Pulse 1 para ver su saldo por pantalla.')
    print('Pulse 2 para imprimir un ticket.')
    visualizacion=int(input())
    if visualizacion == 1:
        print(f'Su saldo disponible es de {saldo_disponible}')
    else:
        imprimir_ticket
    
def conversion_moneda_a_soles(saldo)
    conversion = 0.030834509*saldo
    redondeo = round(conversion, 2)
    return redondeo

def movimientos():
    #funcion que guarda los movimientos de la cuenta.
    return movimientos

def ultimos_movimientos():
    
    print('Pulse 1 para ver su saldo por pantalla.')
    print('Pulse 2 para imprimir un ticket.')
    visualizacion=int(input())
    if visualizacion == 1:
        ultimos_movimientos=movimientos()
        ### aca podria existir una operacion que tome solo los ultimos 10 movimietos.
        print('Sus ultimos 10 movimientos fueron:')
        print(f'{ultimos_movimientos}')
    else:
        imprimir_ticket
    

def consultas():
    print('¿Que operación desea realizar?')
    print('Pulse 1 para consultar su saldo disponible.')
    print('Pulse 2 para consultar sus ultimos movimientos.')
    operacion=int(input())
    clear()
    print('¿Qué tipo de moneda desea utilizar?')
    print('Pulse 1 para seleccionar PESOS.')
    print('Pulse 2 para seleccionar SOLES.')
    moneda=int(input())
    clear()
    if operacion==1:
        resultado=saldo_disponible(saldo)
    elif opcion==2:
        resultado=ultimos_movimientos()
    return resultado
        
        
                