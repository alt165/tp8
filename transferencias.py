"""
Función transferencias
"""

def transferencia(dni, saldo):
    cuenta_destino=input('Ingrese la cuenta destino ')
    saldo=funciones.selecionar_moneda(dni)
    monto=input('Ingrese el monto a transferir')
    if monto <= saldo:
        if cuenta_destino == cliente.cuentra.transferir: #Habria que agregar este dato a la 'base de datos'.
            saldo-=monto
            print('La transferencia se ha realizado con éxito')
        else:
        #retener dinero en cuenta hasta luego de 3 dias, se podria usar simulador para contar los dias en minutos o algo asi.
    else:
        print('No posee saldo suficiente en la cuenta')
        #aca podriamos hacer que le posibilite cambiar el saldo? No lo pide la consigna, pero seria parecido a lo que sucede en extracciones. 
        
    