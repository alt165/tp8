import os, mensajes, clientes, csv, datetime

class saldo_insuficiente_exception(Exception):
    pass

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


def guardar_ticket(ticket):
    """guardar_ticket(str, str) -> file
    esta funcion agrega texto a un archivo con todos los tickets impresos
    """
    with open("tickets.txt", "a") as tickets:
        tickets.write(ticket)
    
def selecionar_moneda(dni):
    print(mensajes.elegir_moneda())
    moneda=input()
    cliente=clientes.cliente(dni)
    if moneda=='1':
        saldo = int(cliente.saldo)
    elif moneda=='2':
        saldo=conversion_moneda_a_soles(cliente.saldo)
    return saldo

def conversion_moneda_a_soles(saldo):
    conversion = 0.030834509* float(saldo)
    conversion = round(conversion, 2)
    return conversion

def obtener_saldo(dni):
    """obtener_saldo(str) -> int
    esta funcion busca el saldo en el archivo con los movimientos de la 
    cuenta del cliente
    """
    ruta = "./movimientos_clientes/" + dni + ".csv"
    with open(ruta, 'r') as f:
        lineas = csv.reader(f)
        for linea in lineas: # no encontré otra forma para iterar el archivo
            pass
    saldo = linea[-2]
    return saldo

def modificar_saldo(dni, movimiento, monto):
    """esta funcion toma los datos de entrada y los agrega el final del
    archivo con los movimientos de cada cliente, los movimientos posibles
    son deposito == "1", extraccion == "2" y transferencia == "3".
    si la extraccion o transferencia es por un monto mayor al saldo
    se levanta una excepción.
    """
    ruta = "./movimientos_clientes/" + dni + ".csv"
    fecha_hora = datetime.datetime.now()
    fecha_hora = fecha_hora.strftime("%m/%d/%Y %H:%M")
    saldo = int(obtener_saldo(dni))
    monto = int(monto)
    if movimiento == "1":
        movimiento = "deposito"
        saldo = saldo + monto
    elif movimiento == "2":
        if monto > saldo:
            raise saldo_insuficiente_exception
        movimiento = "extraccion"
        saldo = saldo - monto
    elif movimiento == "3":
        if monto > saldo:
            raise saldo_insuficiente_exception
        movimiento = "transferencia"
        saldo = saldo - monto
    
    linea = [fecha_hora, movimiento, saldo, monto]
    with open(ruta, 'a') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(linea)


