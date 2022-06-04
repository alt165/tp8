import os, mensajes, clientes

def mensaje_entrada():
    """Esta función muestra el cartel con el nombre del banco
    """
    string_bienvenida = mensajes.nombre_interbanca()
    string_bienvenida = string_bienvenida + "Para utilizar el cajero presione 1:"
    return string_bienvenida

def limita_entrada(mensaje, opcion):
    """Esta funcion muestra el mensaje pasado como argumento
    mientras se ingrese un caracter distinto al argumento opcion
    cuando opcion es igual a la entrada permite continuar
    """
    seguir = True
    while seguir:
        print(mensaje)
        entrada = input()
        if entrada == opcion:
            seguir = False
    
def clear():
    """Funcion para borrar la pantalla"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def leer_tarjeta():
    """Esta función devuelve el dni almacenado
    en la tarjeta, si la tarjeta es válida
    si no devuelve 0"""
    return clientes.cliente_1.dni #tomaremos como válida la tarjeta

def verificar_clave(clave):
    """Esta función devuelve true si la clave es correcta"""
    pass

