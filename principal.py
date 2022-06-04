import funciones, clientes

def principal():
    
    #Mostrar la pantalla inicial
    funciones.limita_entrada(funciones.mensaje_entrada(), "1")
    #el cajero espera que se presione el 1 para permitir avanzar
    
    funciones.clear() #Borrar la pantalla
    print("Inserte su tarjeta")
    dni_tarjeta = funciones.leer_tarjeta()#verificar que sea tarjeta valida y devolver los datos
    if dni_tarjeta != 0:
        dni_cliente = ""
        while dni_cliente != clientes.cliente_1.dni:
            dni_cliente = input("Ingrese su dni")
    print("Ingrese su clave")
        
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
