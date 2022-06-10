def nombre_interbanca():
    """Funcíon que devuelve el cartel con el nombre del banco"""
    interbanca = """

  _____       _            _                           
 |_   _|     | |          | |                          
   | |  _ __ | |_ ___ _ __| |__   __ _ _ __   ___ __ _ 
   | | | '_ \| __/ _ \ '__| '_ \ / _` | '_ \ / __/ _` |
  _| |_| | | | ||  __/ |  | |_) | (_| | | | | (_| (_| |
 |_____|_| |_|\__\___|_|  |_.__/ \__,_|_| |_|\___\__,_|
                                                       
                                                      \n"""
    return interbanca

def menu():
    menu= '''
    Seleccione la opción deseada
    
    1. Consultas.              2. Extracciones.
    3. Transferencias.         4. Salir.  \n'''
    return menu

def menu_consultas():
    consultas= '''
    ¿Que operación desea realizar?
    
    1. Saldo.              2. Movimientos.  \n'''
    return consultas

def elegir_moneda():
    moneda= '''
    Seleccion un tipo moneda:
    
    1. Pesos.              2. Soles.  \n'''
    return moneda


