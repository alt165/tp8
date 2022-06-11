"""
Función extraciones del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

def extraccion(dni):
    print(mensajes.elegir_moneda())
    moneda=input()
    cliente=clientes.cliente(dni)
    saldo=0
    if moneda=='1':
        saldo = cliente.saldo
    elif moneda=='2':
        saldo=conversion_moneda_a_soles(cliente.saldo)
    monto=input('Ingrese el monto a retirar ')
    cuenta_debitar=input('Ingrese la cuenta a debitar ')
    if cuenta_debitar == 
    if monto <= saldo:
        
        
    elif monto > saldo:
        print('No posee saldo suficiente en la cuenta')
        
    