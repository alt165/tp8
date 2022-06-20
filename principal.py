import funciones, clientes, mensajes, consultas, extracciones, transferencias


def principal():
    
    # Mostrar la pantalla inicial
    funciones.limita_entrada(funciones.mensaje_entrada(), "1")
    # el cajero espera que se presione el 1 para permitir avanzar
    
    funciones.clear() #Borrar la pantalla
    
    print("Inserte su tarjeta")
    
    dni_tarjeta = funciones.leer_tarjeta()
    # verificar que sea tarjeta valida y devolver los datos.
    #la funcion leer tarjeta devuelve 0 si la tarjeta no es valida
    
    permite_seguir = True 
    # esta variable se actualizará al verificar las condiciones que permiten
     # continuar utilizando el cajero
    
    if dni_tarjeta != 0: #si la tarjeta es válida
        dni_cliente = ""
        intentos_posibles = 3
        intento = 0
        while dni_cliente != dni_tarjeta and intento < intentos_posibles:
            dni_cliente = input("Ingrese su dni: ")
            intento = intento + 1
        if intento > intentos_posibles:
            permite_seguir = False # llegamos a la cantidad permitida de intentos
            print("Ha superado la cantidad de ingresos posibles")
            print("Retire su tarjeta")
    else:
        permite_seguir = False # No se ingresó una tarjeta válida
    
    if permite_seguir: #si la tarjeta es valida y el dni es correcto, obtener clave
        clave_almacenada = funciones.obtener_clave(dni_cliente)
        #buscar clave almacenada
        intentos_posibles = 3
        intento = 0
        clave_cliente = ""
        while clave_cliente != clave_almacenada and intento < intentos_posibles:
            clave_cliente = input("Ingrese su clave: ")
            intento = intento + 1
        if intento > intentos_posibles: 
            #luego de tres intentos retener tarjeta y finalizar
            print("Ha superado la cantidad de ingresos posibles")
            print("Su tarjeta ha sido retenida")
            permite_seguir = False
            retener_tarjeta = True
        cliente = clientes.cliente(dni_cliente)
            
    continuar=True # solo se actualiza cuando el cliente quiere salir
    while permite_seguir and continuar:
        funciones.clear()
        print(mensajes.menu())
        opcion=input('')
        if opcion == "1":
            funciones.clear()
            print(mensajes.menu_consultas())
            operacion=input()
            funciones.clear()
            if operacion=='1':
                saldo=consultas.consultar_saldo(cliente.dni)
                ticket = funciones.formatear_ticket("\tSu saldo es: ", saldo)
                print(ticket)
                if mensajes.quiere_imprimir_ticket():
                    funciones.guardar_ticket(ticket)
            elif operacion=='2':
                ticket = consultas.ultimos_movimientos(cliente.dni)
                print(ticket)
                if mensajes.quiere_imprimir_ticket():
                    funciones.guardar_ticket(ticket)

            
        elif opcion == "2":
            funciones.clear()
            monto = input("Ingrese el monto a extraer: ")
            try:
                ticket = extracciones.extraccion(cliente.dni, monto)
                if mensajes.quiere_imprimir_ticket():
                    funciones.guardar_ticket(ticket)
            except funciones.saldo_insuficiente_exception:
                print("El monto seleccionado es mayor al saldo")
                input("Presione enter para continuar")
            
        elif opcion == "3":
            funciones.clear()
            monto = input("Ingrese el monto a tranferir: ")
            destino = input("Ingrese la cuenta destino: ")
            # no se va a verificar la cuenta destino, cualquier ingreso lo tomamos como válido 
            try:
                ticket = transferencias.transferencia(cliente.dni, monto, destino)
                if mensajes.quiere_imprimir_ticket():
                    funciones.guardar_ticket(ticket)
            except funciones.saldo_insuficiente_exception:
                print("El monto seleccionado es mayor al saldo")
                input("Presione enter para continuar")
            
    
            
        elif opcion == "4":
            print(mensajes.mensaje_salir())
            continuar=False

     
if __name__ == "__main__":
    principal()
    
