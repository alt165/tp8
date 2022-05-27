def mensaje_entrada():
    string_bienvenida = """

  _____       _            _                           
 |_   _|     | |          | |                          
   | |  _ __ | |_ ___ _ __| |__   __ _ _ __   ___ __ _ 
   | | | '_ \| __/ _ \ '__| '_ \ / _` | '_ \ / __/ _` |
  _| |_| | | | ||  __/ |  | |_) | (_| | | | | (_| (_| |
 |_____|_| |_|\__\___|_|  |_.__/ \__,_|_| |_|\___\__,_|
                                                       
                                                       
Para utilizar el cajero presione 1:
"""
    return string_bienvenida

def menu_inicial():
    seguir = True
    uno = ""
    while seguir != False:
        print(mensaje_entrada())
        uno = input()
        if uno == "1":
            seguir = False

def leer_tarjeta():
    """Esta función devuelve True si la tarjeta es válida
    si no lo es devuelve False"""
    pass

def verificar_clave(clave):
    """Esta función devuelve true si la clave es correcta"""
    pass

