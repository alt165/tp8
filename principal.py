import funciones, clientes, mensajes, consultas

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
    
    if dni_tarjeta != 0: 
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
    
    if permite_seguir: #si la tarjeta es valida y el dni es correcto
        clave_almacenada = funciones.obtener_clave(dni_cliente)
        intentos_posibles = 3
        intento = 0
        clave_cliente = ""
        while clave_cliente != clave_almacenada and intento < intentos_posibles:
            clave_cliente = input("Ingrese su clave: ")
            intento = intento + 1
        if intento > intentos_posibles:
            print("Ha superado la cantidad de ingresos posibles")
            print("Su tarjeta ha sido retenida")
            permite_seguir = False
            retener_tarjeta = True
        cliente = clientes.cliente(dni_cliente)
        print(cliente.saldo)
    
    continuar=True
    while permite_seguir and continuar:
        funciones.clear()
        print(mensajes.menu())
        opcion=input('')
        if opcion == "1":
            consultas.consultas(dni_cliente)    
        elif opcion == "2":
            print('2')
        elif opcion == "3":
            print('3')
        elif opcion == "4":
            print('4')
            continuar=False
        #tomar opcion de menu
    #    if opcion extraccion:
     #       monto
      #      funcion_extraccion()
       #     funcion_continuar()
        #elif opcion == consultas:
        #    funcion_consultas()
         #   funcion_continuar()
 #       elif opcion == transferencias:
  #          funcion_transferencias()
   #         funcion_continuar()
    #    else:
     #       salir()
     
if __name__ == "__main__":
    principal()
    
