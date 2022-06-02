import funciones

def principal():
        
    funciones.menu_inicial() #mostrar el menu de espera
    funciones.clear()
    print("Inserte su tarjeta")
    if funciones.leer_tarjeta():#verificar que sea tarjeta valida y devolver los datos
        pass
        
    pedir_dni()
    pedir_clave()
    verificar_dni_clave()
    #si verificar dni y clave se ejecuto tres veces retener tarjeta
    #else:
    while seguir:
        mostrar_menu()
        #tomar opcion de menu
        if opcion extraccion:
            monto
            funcion_extraccion()
            funcion_continuar()
        elif opcion == consultas:
            funcion_consultas()
            funcion_continuar()
        elif opcion == transferencias:
            funcion_transferencias()
            funcion_continuar()
        else:
            salir()