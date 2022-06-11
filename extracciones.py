"""
Función extraciones del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

def extraccion(dni):
    print(mensajes.elegir_moneda())
    moneda=input()
    cliente=clientes.cliente(dni)
    if moneda=='1':
        saldo = int(cliente.saldo)
    elif moneda=='2':
        saldo=conversion_moneda_a_soles(cliente.saldo)
    intento=0
    while intento < 2:
        monto=int(input('Ingrese el monto a retirar '))
        intento+=1
        if monto <= saldo:
            cliente.saldo-=monto #no funciona, saldo no disminuye y es str contra int.
            intento+=1
        elif monto > saldo:
            print('No posee saldo suficiente en la cuenta.') #no se como hacer para que en la segunda vez ingresado un monto mayor no muestre las opciones siguientes. 
            print('1.Modificar monto.           2.Volver al menú de opciones.')
            eleccion=input()
            if eleccion =='2':
                intento+=1    
            
                
            
def conversion_moneda_a_soles(saldo): #traje esta funcion aqui si no decia que no estaba definida. Intente importarla pero no funciona.
    conversion = 0.030834509* float(saldo)
    conversion = round(conversion, 2)
    return conversion
     
    