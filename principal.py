import funciones, clientes

def principal():
    
    # Mostrar la pantalla inicial
    funciones.limita_entrada(funciones.mensaje_entrada(), "1")
    # el cajero espera que se presione el 1 para permitir avanzar
    
    funciones.clear() #Borrar la pantalla
    
    print("Inserte su tarjeta")
    
    dni_tarjeta = funciones.leer_tarjeta()# verificar que sea tarjeta valida y devolver los datos
    permite_seguir = True # esta variable se actualizará al verificar las condiciones que permiten
                          # continuar utilizando el cajero
    if dni_tarjeta != 0:
        dni_cliente = ""
        intentos_posibles = 3
        intento = 0
        while dni_cliente != dni_tarjeta and intento < intentos_posibles:
            dni_cliente = input("Ingrese su dni: ")
            intento = intento + 1
        if intento == 2:
            permite_seguir = False # llegamos a la cantidad permitida de intentos
    else:
        permite_seguir = False # No se ingresó una tarjeta válida
    
    clave_almacenada = funciones.obtener_clave
    intentos_posibles = 3
    intento = 0
    clave_cliente = ""
    while clave_cliente != clave_almacenada and intento < intentos_posibles:
        clave_cliente = input("Ingrese su clave: ")
        intento = intento + 1
    if intento == 2:
        permite_seguir = False
        retener_tarjeta = True
    #if verificar_clave(dni_cliente, 3):
     #   clave_cliente = input(print("Ingrese su clave:"))
    #print(verificar_clave(clave_cliente)) 
    cliente = funciones.obtener_cliente(dni_cliente)
    print(cliente.saldo)

    #pedir_clave()
    #verificar_dni_clave()
    #si verificar dni y clave se ejecuto tres veces retener tarjeta
    #else:
    #while seguir:
    #    mostrar_menu()
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
    
