import csv


class Cliente:
    """Clase de tipo cliente con los datos
    necesarios para identificarlos
    """
    def __init__(self, nombre, dni, clave, saldo):
        self.nombre = nombre
        self.dni = dni
        self.clave = clave
        self.saldo = saldo


def cliente(dni):
    """Esta funcion busca en el archivo de clientes y devuelve un objeto
    con los atributos del cliente encontrado"""
    coincidencia=[]
    with open("lista_de_clientes.csv", 'r') as archivo:
        mis_clientes = csv.reader(archivo)
        for line in mis_clientes:
            if line[1] == dni:
                coincidencia = line
    
    cliente_encontrado = Cliente(coincidencia[0],coincidencia[1],coincidencia[2],coincidencia[3])
    return cliente_encontrado
