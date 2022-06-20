"""
Función transferencias
"""
import funciones

def transferencia(dni, monto, destino):
    funciones.modificar_saldo(dni, "3", monto)
    saldo = funciones.obtener_saldo(dni)
    ticket = funciones.formatear_ticket(f"Transfirió {monto}\n", f"A la cuenta: {destino}")
    print(ticket)
    return ticket
