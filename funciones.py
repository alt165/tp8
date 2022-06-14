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
    en la tarjeta si la tarjeta es válida
    si no devuelve 0"""
    return "12345678" 
    # tomaremos como válida la tarjeta. No está implementada la función
    # no tenemos forma de leer una tarjeta, solo devolvemos el dni del
    # cliente que elegimos para trabajar


def obtener_clave(dni_cliente):
    """verificar_clave()
    Esta función busca la clave almacenada en la lista de clientes
    """    
    cliente = clientes.cliente(dni_cliente)
    return cliente.clave

def formatear_ticket(texto1, texto2):
    """formatear_ticket(str, str) -> str
    esta funcion devuelve un string con el texto formateado de un ticket
     """
    ticket = mensajes.encabezado_ticket()
    ticket = ticket + texto1
    ticket = "\n" + ticket + texto2 + "\n"

    return ticket


def guardar_ticket(archivo, ticket):
    """guardar_ticket(str, str) -> file
    esta funcion agrega texto a un archivo con todos los tickets impresos
    """
    
def selecionar_moneda(dni)
    print(mensajes.elegir_moneda())
    moneda=input()
    cliente=clientes.cliente(dni)
    if moneda=='1':
        saldo = int(cliente.saldo)
    elif moneda=='2':
        saldo=conversion_moneda_a_soles(cliente.saldo)
    return saldo
