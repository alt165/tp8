"""
Función consultas del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

#nota: todas las funciones que impliquen cambios en el saldo afectarian a movimientos.

def tipo_moneda():
    print('¿Qué tipo de moneda desea utilizar?')
    print('Pulse 1 para seleccionar PESOS.')
    print('Pulse 2 para seleccionar SOLES.')
    moneda=int(input())
    return moneda

def saldo(dni):
    #esta funcion guardaria los saldos, y una vez que se invoca una extracion deberia cambiar.
    cliente=funciones.obtener_cliente(dni)
    saldo=cliente.saldo
    return saldo

def saldo_disponible(moneda):
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
    
#def conversion_moneda_a_soles(saldo)
 #   conversion = 0.030834509*saldo
 #   redondeo = round(conversion, 2)
  #  return redondeo

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
    

def consultas(dni):
    
    print(mensajes.menu_consultas())
    operacion=input()
    funciones.clear()
    print(mensajes.elegir_moneda())
    moneda=input()
    #if operacion=="1":
     #   saldo=(saldo_disponible(dni))
        
      #  if moneda=="1":
       #     print(saldo
        
        
    #elif opcion=="2":
     #  resultado=ultimos_movimientos()
    #return resultado
        
        
                