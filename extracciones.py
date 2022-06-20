"""
Función extraciones del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

def extraccion(dni, monto):
    funciones.modificar_saldo(dni, "2", monto)
    saldo = funciones.obtener_saldo(dni)
    ticket = funciones.formatear_ticket(f"Retiró {monto}\n", f"Su saldo es: {saldo}")
    print(ticket)
    return ticket
    

            
                
            
     
    