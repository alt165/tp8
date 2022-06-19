"""
Función extraciones del menú perteneciente al Cajero Automatico InterBanca TP INTEGRADOR IIC.
"""
import funciones, clientes, mensajes

def extraccion(dni):
    saldo=funciones.selecionar_moneda(dni)
    intento=0
    while intento < 2:
        monto=int(input('Ingrese el monto a retirar '))
        intento+=1
        if monto <= saldo:
            cliente.saldo-=monto #no funciona, saldo no disminuye y es str contra int.
            intento+=1
        elif monto > saldo:
            print('No posee saldo suficiente en la cuenta.') #no se como hacer para que en la segunda vez ingresado un monto mayor no muestre las opciones siguientes. 
            if intento < 2:
                print('1.Modificar monto.           2.Volver al menú de opciones.')
                eleccion=input()
                if eleccion =='2':
                    intento+=1    
            
                
            
     
    