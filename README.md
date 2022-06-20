# Trabajo Práctico Integrador
*** 
## __Integrantes:__

#### Luz Tranzillo.
#### José Lambrechts

***
# Interbanca

La consigna de este trabajo es implementar las funciones básicas de un cajero automático.
Se crea un cliente ficticio con el que se trabaja. El flujo de funcionamiento comienza con el cajero en espera y continua cuando se solicita el DNI y clave de este usuario. A continuacion se muestra el menú de opciones. Las posibilidades son las siguientes:
 * Consultas
    * Saldo (permite elegir entre pesos o soles)
    * Movimientos
* Extracciones
* Transferencias
* Salir

Estas opciones muestran un ticket por pantalla y luego pregunta si lo quiere imprimir. En caso de imprimirlo se guarda el ticket en un archivo llamado *tickets.txt*.
Las operaciones que impliquen modificaciones en el saldo del cliente se guardan en el directorio *movimientos_clientes* en un archivo csv llamado con el dni del cliente