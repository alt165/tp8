"""
Función consultas del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

#nota: todas las funciones que impliquen cambios en el saldo afectarian a movimientos.

def consultar_saldo(dni):
    print(mensajes.elegir_moneda())
    moneda=input()
    cliente=funciones.obtener_cliente(dni.cliente)
    saldo=cliente.saldo
    if moneda=='1':
        pass
    elif moneda=='2':
        saldo=conversion_moneda_a_soles(saldo)
    return saldo
    
def conversion_moneda_a_soles(saldo):
    conversion = 0.030834509*saldo
    return conversion


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
    
def movimientos():
    #funcion que guarda los movimientos de la cuenta.
    return movimientos



        
        
                