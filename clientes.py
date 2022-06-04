class Cliente:
    """Clase de tipo cliente con los datos
    necesarios para identificarlos
    """
    def __init__(self, nombre, dni, clave, saldo):
        self.nombre = nombre
        self.dni = dni
        self.clave = clave
        self.saldo = saldo

cliente_1 = Cliente("Roberto Arlt", "12345678", "12345", 85000)