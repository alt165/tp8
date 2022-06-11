import datetime

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
    Seleccione un tipo moneda:
    
    1. Pesos.              2. Soles.  \n'''
    return moneda

def encabezado_ticket():
    encabezado = """
    ******************************
            Interbanca
    ******************************\n
       """
    fecha_hora = datetime.datetime.now()
    fecha_hora = fecha_hora.strftime("%c")    
    encabezado = encabezado + fecha_hora + "\n\n"
    

    return encabezado

def quiere_continuar():
    continuar = True
    while continuar:
        input("Para continuar presione una tecla ")
        continuar = False