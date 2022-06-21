Diagrama de flujo función PRINCIPAL.

```mermaid
graph 
    a(inicio)-->b["funciones.limita_entrada(funciones.mensaje_entrada(), '1')"]
    b-->c["funciones.clear()"]
    c-->d("print('Inserte su tarjeta')")
    d-->e["dni_tarjeta = funciones.leer_tarjeta()"]
    e-->f[" permite_seguir = True "]
    f-->g{"if dni_tarjeta != 0: "}
    g-->|si|h["dni_cliente = ' '"]
    h-->i[intentos_posibles = 3]
    i-->j[ intento = 0]
    j-->k["while dni_cliente != dni_tarjeta and intento < intentos_posibles:"]
    k-->l["dni_cliente = input('Ingrese su dni: ')"]
    l-->m[ intento = intento + 1]
    m-->k
    k-->n{"if intento > intentos_posibles:"}
    n-->|si|ñ["permite_seguir = False"]
    ñ-->o("print('Ha superado la cantidad de ingresos posibles')")
    o-->p("print('Retire su tarjeta')")
    p-->ZZ(FIN)
    g-->|no|q[" permite_seguir = False"]
    q-->ZZ
    n-->|no|r{permite_seguir: }
    r-->|si|s["clave_almacenada = funciones.obtener_clave(dni_cliente)"]
    s-->t["intentos_posibles = 3"]
    t-->v["intento = 0"]
    v-->w["clave_cliente = ' ' "]
    w-->x["while clave_cliente != clave_almacenada and intento < intentos_posibles:"]
    x-->y["clave_cliente = input('Ingrese su clave: ')"]
    y-->aa["intento = intento + 1"]
    aa-->x
    x-->bb{"intento > intentos_posibles: "}
    bb-->|si|cc("print('Ha superado la cantidad de ingresos posibles')")
    cc-->dd(" print('Su tarjeta ha sido retenida')")
    dd-->ee["permite_seguir = False"]
    ee-->ff["retener_tarjeta = True"]
    ff-->ZZ
    bb-->|no|gg["cliente = clientes.cliente(dni_cliente)"]
    gg-->hh[continuar=True]
    hh-->jj["while permite_seguir and continuar:"]
    jj-->kk["funciones.clear()"]
    kk-->ll("print(mensajes.menu())")
    ll-->mm[/"opcion=input('')"/]
    mm-->nn{"if opcion == '1':"}
    nn-->|si|qq["funciones.clear()"]
    qq-->qq1("print(mensajes.menu())")
    qq1-->qq2[/"operacion=input()"/]
    qq2-->qq3{"operacion=='1'"}
    qq3-->|si|qq4["saldo=consultas.consultar_saldo(cliente.dni)"]
    qq4-->qq5["ticket = funciones.formatear_ticket('\tSu saldo es: ', saldo)"]
    qq5-->qq6("print(ticket)")
    qq6-->qq7{"mensajes.quiere_imprimir_ticket():"}
    qq7-->|si|qq8["funciones.guardar_ticket(ticket)"]
    qq8-->jj
    qq7-->|no|jj
    qq3-->|no|qq9{operacion=='2':}
    qq9-->|si|qq10["ticket = consultas.ultimos_movimientos(cliente.dni)"]
    qq10-->qq11("print(ticket)")
    qq11-->qq12{"mensajes.quiere_imprimir_ticket():"}
    qq12-->|si|qq13["funciones.guardar_ticket(ticket)"]
    qq13-->jj
    qq12-->|no|jj
    nn-->|no|oo{"elif opcion == '2':"}
    oo-->|si|rr["funciones.clear()"]
    rr-->rr1[/"monto = input('Ingrese el monto a extraer: ')"/]
    rr1-->rr2["try:"]
    rr2-->rr3["ticket = extracciones.extraccion(cliente.dni, monto)"]
    rr3-->rr4{"if mensajes.quiere_imprimir_ticket():"}
    rr4-->|si|rr5["funciones.guardar_ticket(ticket)"]
    rr5-->jj
    rr4-->|no|jj
    rr2-->rr6["funciones.saldo_insuficiente_exception:"]
    rr6-->rr7("print('El monto seleccionado es mayor al saldo')")
    rr7-->rr8[/"input('Presione enter para continuar')"/]
    oo-->|no|ss{"opcion == '3':"}
    ss-->|si|ss1["funciones.clear()"]
    ss1-->ss2[/"monto = input('Ingrese el monto a tranferir: ')"/]
    ss2-->ss3[/"destino = input('Ingrese la cuenta destino: ')"/]
    ss3-->ss4["try:"]
    ss4-->ss5["ticket = transferencias.transferencia(cliente.dni, monto, destino)"]
    ss5-->ss6{"mensajes.quiere_imprimir_ticket():"}
    ss6-->|no|jj
    ss6-->|si|ss7["funciones.guardar_ticket(ticket)"]
    ss7-->jj
    ss4-->ss8{"funciones.saldo_insuficiente_exception:"}
    ss8-->ss9("print('El monto seleccionado es mayor al saldo')")
    ss9-->ss10[/"input('Presione enter para continuar')"/]
    ss10-->jj
    ss-->|no|uu{"opcion == '4':"}
    uu-->|si|uu1("print(mensajes.mensaje_salir())")
    uu1-->uu2["continuar=False"]
    uu-->jj
    jj-->ZZ
```

Grafo de complejidad función PRINCIPAL.

```mermaid
graph 
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
    f-->|VI|g((7))
    g-->|si-VII|h((8))
    h-->|VIII|i((9))
    i-->|IX|j((10))
    j-->|X|k((11))
    k-->|XI|l((12))
    l-->|XII|m((13))
    m-->|XIII|k
    k-->|XIV|n((14))
    n-->|si-XV|ñ((15))
    ñ-->|XVI|o((16))
    o-->|XVII|p((17))
    p-->|XVIII|ZZ((18))
    g-->|no-XIX|q((19))
    q-->|XX|ZZ
    n-->|no-XXI|r((20))
    r-->|si-XXII|s((21))
    s-->|XXIII|t((22))
    t-->|XXIV|v((23))
    v-->|XXV|w((24))
    w-->|XXVI|x((25))
    x-->|XXVII|y((26))
    y-->|XXVIII|aa(27)
    aa-->|XXIX|x
    x-->|XXX|bb((28))
    bb-->|si-XXXI|cc((29))
    cc-->|XXXII|dd((30))
    dd-->|XXXIII|ee((31))
    ee-->|XXXIV|ff((32))
    ff-->|XXXV|ZZ
    bb-->|no-XXXVI|gg((33))
    gg-->|XXXVII|hh((34))
    hh-->|XXXVIII|jj((35))
    jj-->|XXXIX|kk((36))
    kk-->|XXXX|ll((37))
    ll-->|XXXXI|mm((38))
    mm-->|XXXXII|nn((39))
    nn-->|si-XXXXIII|qq((40))
    qq-->|XXXXIV|qq1((41))
    qq1-->|XXXXV|qq2((42))
    qq2-->|XXXXVI|qq3((43))
    qq3-->|si-XXXXVII|qq4((44))
    qq4-->|XXXXVIII|qq5((45))
    qq5-->|XXXXIX|qq6((46))
    qq6-->|L|qq7((47))
    qq7-->|si-LI|qq8((48))
    qq8-->|LII|jj
    qq7-->|no-LIII|jj
    qq3-->|no-LIV|qq9((49))
    qq9-->|si-LV|qq10((50))
    qq10-->|LVI|qq11((51))
    qq11-->|LVII|qq12((52))
    qq12-->|si-LVIII|qq13((53))
    qq13-->|LIX|jj
    qq12-->|no-LX|jj
    nn-->|no-LXI|oo((54))
    oo-->|si-LXII|rr((55))
    rr-->|LXIII|rr1((56))
    rr1-->|LXIV|rr2((57))
    rr2-->|LXV|rr3((58))
    rr3-->|LXVI|rr4((59))
    rr4-->|si-LXVII|rr5((60))
    rr5-->|LXVIII|jj
    rr4-->|no-LXIX|jj
    rr2-->|LXX|rr6((61))
    rr6-->|LXXI|rr7((62))
    rr7-->|LXXII|rr8((63))
    oo-->|no-LXXIII|ss((64))
    ss-->|si-LXXIV|ss1((65))
    ss1-->|LXXV|ss2((66))
    ss2-->|LXXVI|ss3((67))
    ss3-->|LXXVII|ss4((68))
    ss4-->|LXXVIII|ss5((69))
    ss5-->|LXXIX|ss6(70)
    ss6-->|no-LXXX|jj
    ss6-->|si-LXXXI|ss7((71))
    ss7-->|LXXXII|jj
    ss4-->|LXXXIII|ss8((72))
    ss8-->|LXXXIV|ss9((73))
    ss9-->|LXXXV|ss10((74))
    ss10-->|LXXXVI|jj
    ss-->|no-LXXXVII|uu((75))
    uu-->|si-LXXXVIII|uu1((76))
    uu1-->|LXXXIX|uu2((77))
    uu-->|LXXXX|jj
    jj-->|LXXXXI|ZZ
```

Calculos complejidad cilomatica función PRINCIPAL:

-V(G)=Regiones=16.\
-V(G)=A-N+2=91-77+2=16.\
-V(G)=P+1=15+1=16

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Diagrama de flujo función EXTRACCIONES. 

```mermaid
graph 
    a((inicio))-->b["funciones.modificar_saldo(dni, '2', monto)"]
    b-->c["saldo = funciones.obtener_saldo(dni)"]
    c-->d["ticket = funciones.formatear_ticket(f'Retiró {monto}\n', f'Su saldo es: {saldo}')"]
    d-->e(" print(ticket)")
    e-->f(fin-return ticket)

  ```

Grafo de complejidad función EXTRACCIONES.

```mermaid
graph 
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
```  

Calculos complejidad cilomatica función EXTRACCIONES:

-V(G)=Regiones=1.\
-V(G)=A-N+2=5-6+2=.1\
-V(G)=P+1=0+1=1.

Caminos posibles función EXTRACCIONES:

-1-2-3-4-5-6

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función CLIENTES:

```mermaid 
graph 
   A((Inicio)) --> B["coincidencia=[]"]
    B-->C[with open]
    C-->D["mis clientes = cvs.reader(archivo)"]
    D-->E[for line in mis_clientes:]
    E-->F{"line[1]==dni"}
    F-->|si|G[coincidencia = line]
    G-->E
    E-->I["cliente_encontrado=cliente(coincidencia[0],(coincidencia[1],(coincidencia[2],(coincidencia[3])"]
    I-->H(FIN - return cliente_encontrado)
```

Grafo de complejidad ciclomatica función CLIENTES:

```mermaid 
graph 
    A((1)) -->|I| B((2))
    B-->|II|C((3))
    C-->|III|D((4))
    D-->|IV|E((5))
    E-->|V|F((6))
    F-->|si-VI|G((7))
    G-->|VII|E
    E-->|VIII|I((8))
    I-->|IX|J((9))

style E fill:#909
```
Calculos complejidad cilomatica función CLIENTES:

-V(G)=Regiones=2.\
-V(G)=A-N+2=9-9+2=2.\
-V(G)=P+1=1+1=2.

Caminos posibles función CLIENTES:

-1-2-3-4-5-6-7-8-9.\
-1-2-3-4-5-8-9

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo función CONSULTAS:

```mermaid
graph 
a((Inicio))-->b("print('mensajes.elegir_moneda())")
b-->c[/"moneda=input()"/]
c-->d["saldo=funciones.obtener_saldo(dni)"]
d-->e{moneda=='1':}
e-->|si|f["saldo=str(saldo)+'Pesos'"]
e-->|no|g{moneda=='2':}
g-->|si|h["saldo=str(funciones.conversion_moneda_a_soles(saldo))+'Soles'"]
f-->i((fin - return saldo))
h-->i
```

Grafo de complejidad ciclomatica función CONSULTAS:

```mermaid
graph 
a((1))-->|I|b((2))
b-->|II|c((3))
c-->|III|d((4))
d-->|IV|e((5))
e-->|si-V|f((6))
e-->|no-VII|g((8))
g-->|si-VIII|h((9))
f-->|VI|i((7))
h-->|IX|i

style e fill:#909
```
Calculos complejidad cilomatica función CONSULTAS:

-V(G)=Regiones=2.\
-V(G)=A-N+2=9-9+2=2.\
-V(G)=P+1=1+1=2

Caminos posibles función CONSULTAS:
-1-2-3-4-5-6-7\
-1-2-3-4-5-8-9-7

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función ULTIMOS_MOVIMIENTOS:

```mermaid
graph 
a((inicio))-->b["ruta='./movimientos_clientes/' + dni + '.csv'"]
b-->c["with open(ruta, 'r') as movimientos:"]
c-->d["archivo = movimientos.readlines()"]
d-->f["largo=len(archivo)"]
f-->g["resultado = funciones.formatear_ticket('Fecha     Movimiento    Saldo    Monto',' ')"]
g-->h{largo>10:}
h-->|si|i[largo=-10]
h-->|no|j[largo*-1]
i-->z[largo=-1]
z-->k[while largo<0:]
j-->z
k-->l["resultado=resultado+archivo[archivo]"]
l-->m[largo=largo+1]
m-->k
k-->n(fin - return resultado)
```

Grafo de complejidad ciclomatica función ULTIMOS_MOVIMIENTOS:

```mermaid
graph 
a((1))-->|I|b((2))
b-->|II|c((3))
c-->|III|d((4))
d-->|IV|f((5))
f-->|V|g((6))
g-->|VI|h((7))
h-->|si-VII|i((8))
h-->|no-XIV|j((14))
i-->|VIII|z((9))
z-->|IX|k((10))
j-->|XV|z
k-->|X|l((11))
l-->|XI|m((12))
m-->|XII|k
k-->|XIII|n((13))

style k fill:#909
style h fill:#909

```

Calculos complejidad cilomatica función ULTIMOS_MOVIMIENTOS:

-V(G)=Regiones=3.\
-V(G)=A-N+2=15-14+2=3.\
-V(G)=P+1=2+1=3

Caminos posibles función ULTIMOS_MOVIMIENTOS:

-1-2-3-4-5-6-7-8-9-10-11-12-13.\
-1-2-3-4-5-6-7-14-9-10-11-12-13.\
-1-2-3-4-5-6-7-8-9-10-13.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo función MENSAJE_ENTRADA del apartado funciones:

```mermaid
graph 
    a((inicio))-->b["string_bienvenida = mensajes.nombre_interbanca()"]
    b-->c["string_bienvenida = string_bienvenida + 'Para utilizar el cajero presione 1:'"]
    c-->d(fin-return string_bienvenida)
```    

Grafo de complejidad ciclomatica función MENSAJE_ENTRADA del apartado funciones:

```mermaid
graph 
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
```
Calculos complejidad cilomatica función MENSAJE_ENTRADA del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=3-4+2=1.\
-V(G)=P+1=0+1=1

Caminos posibles función MENSAJE_ENTRADA del apartado funciones:

-1-2-3-4

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función LIMITA_ENTRADA del apartado funciones:

```mermaid
graph 
    a((inicio))-->b[seguir=True]
    b-->c[while seguir:]
    c -->d("print(mensaje)")
    d-->e[/"entrada=input()"/]
    e-->f{"entrada==opcion:"}
    f-->|si|g["seguir=False"]
    g-->c
    c-->h((fin))
    f-->c
    
```

Grafo de complejidad de la función LIMITA_ENTRADA del apartado funciones:

```mermaid
graph 
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c -->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
    f-->|si-VI|g((7))
    g-->|VIII|c
    c-->|VII|h((8))
    f-->|IX|c
    
     style c fill:#909
```

Calculos complejidad cilomatica función LIMITA_ENTRADA del apartado funciones:

-V(G)=Regiones=2.\
-V(G)=A-N+2=9-8+2=3.\
-V(G)=P+1=1+1=2.

Caminos posibles función LIMITA_ENTRADA del apartado funciones:

-1-2-3-4-5-6-7-3-8\
-1-2-3-4-5-6-3-4-5-6-7-3-8

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función CLEAR del apartado funciones:

```mermaid
graph
    a((inicio))-->b{os.name=='nt':}
    b-->|si|c["os.system('cls')"]
    b-->|no|d["os.system('clear')"]
    c-->e((fin))
    d-->e
    
```

Grafo de complejidad de la función CLEAR del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|si-II|c((3))
    b-->|no-IV|d((5))
    c-->|III|e((4))
    d-->|V|e
    
    style b fill:#909
```

Calculos complejidad cilomatica función CLEAR del apartado funciones:

-V(G)=Regiones=2.\
-V(G)=A-N+2=5-5+2=2.\
-V(G)=P+1=1+1=2.

Caminos posibles función CLEAR del apartado funciones:

-1-2-3-4\
-1-2-5-4

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función OBTENER_CLAVE del apartado funciones:

```mermaid
graph
    a((inicio))-->b["cliente=clientes.cliente(dni_cliente)"]
    b-->c(fin-return cliente.clave)
``` 

Grafo de complejidad de la función OBTENER_CLAVE del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
``` 
Calculos complejidad cilomatica función OBTENER_CLAVE del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=2-3+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función OBTENER_CALVE del apartado funciones:

-1-2-3.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función FORMATEAR_TICKET del apartado funciones:

```mermaid
graph
    a((inicio))-->b["ticket = mensajes.encabezado_ticket()"]
    b-->c[ticket = ticket + texto1]
    c-->d["ticket= '\n' + ticket + texto2 + '\n'"]
    d-->element((fin))
   
```

Grafo de complejidad ciclomatica de la función FORMATEAR_TICKET del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
```

Calculos complejidad cilomatica función FORMATEAR_TICKET del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=4-5+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función FORMATEAR_TICKET del apartado funciones:

-1-2-3-4-5

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función GUARDAR_TICKET del apartado funciones:

```mermaid
graph
    a((inicio))-->b["with open('tickets.txt', 'a') as tickets:"]
    b-->c["tickets.write(ticket)"]
    c-->d((fin))
```

Grafo de complejidad ciclomatica de la función GUARDA_TICKET del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
```

Calculos complejidad cilomatica función GUARDAR_TICKET del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=3-4+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función GUARDAR_TICKET del apartado funciones:

-1-2-3-4.
   
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función SELECCIONAR_MONEDA del apartado funciones:

```mermaid
graph
    a((inicio))-->b("print(mensajes.elegir_moneda()) ")
    b-->c[/"moneda=input()"/]
    c-->d["cliente=clientes.cliente(dni)"]
    d-->e{"moneda=='1':"}
    e-->|si|f["saldo=int(cliente.saldo)"]
    e-->|no|g{"moneda=='2':"}
    g-->|si|h["saldo=conversion_moneda_a_soles(cliente.saldo)"]
    h-->i(fin - return saldo)
    f-->i
```

Grafo de complejidad ciclomatica de la función SELECCIONAR_MONEDA del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|si-V|f((6))
    e-->|no-VII|g((8))
    g-->|si-VIII|h((9))
    h-->|IX|i((7))
    f-->|VI|i

style e fill:#909
```

Calculos complejidad cilomatica función SELECCIONAR_MONEDA del apartado funciones:

-V(G)=Regiones=2.\
-V(G)=A-N+2=9-9+2=2.\
-V(G)=P+1=1+1=2.

Caminos posibles función SELECCIONAR_MONEDA del apartado funciones:

-1-2-3-4-5-6-7.\
-1-2-3-4-5-8-9-7.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función CONVERSION_MONEDA_A_SOLES del apartado funciones:

```mermaid
graph
    a((inicio))--> b["conversion = 0.030834509* float(saldo)"]
    b-->c["conversion = round(conversion, 2)"]
    c-->d(fin - return conversion)
```

Grafo de complejidad ciclomatica de la función CONVERSION_MONEDA_A_SOLES del apartado funciones:

```mermaid
graph
    a((1))-->|I| b((2))
    b-->|II|c((3))
    c-->|III|d((4))
```

Calculos complejidad cilomatica función CONVERSION_MONEDA_A_SOLES del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=3-4+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función CONVERSION_MONEDA_A_SOLES del apartado funciones:

-1-2-3-4.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función OBTENER_SALDO del apartado funciones:

```mermaid
graph
    a((inicio))-->b["ruta = './movimientos_clientes/' + dni + '.csv'"]
    b-->c["with open(ruta, 'r') as f:"]
    c-->d["lineas = csv.reader(f)"]
    d-->e[for linea in lineas:]
    e-->f[pass]
    f-->e
    e-->g["saldo=linea[-2]"]
    g-->h(fin-return saldo)
```

Grafo de complejidad ciclomatica de la función OBTENER_SALDO del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
    f-->|VI|e
    e-->|VII|g((7))
    g-->|VIII|h((8))

style e fill:#909
```

Calculos complejidad cilomatica función OBTENER_SALDO del apartado funciones:

-V(G)=Regiones=2.\
-V(G)=A-N+2=8-8+2=2.\
-V(G)=P+1=1+1=2.

Caminos posibles función OBTENER_SALDO del apartado funciones:

-1-2-3-4-5-6-7-8\
-1-2-3-4-5-6-5-6-7-8

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función MODIFICAR_SALDO del apartado funciones:

```mermaid
graph
    a((inicio))-->b["ruta = './movimientos_clientes/' + dni + '.csv'"]
    b-->c["fecha_hora = datetime.datetime.now()"]
    c-->d["fecha_hora = fecha_hora.strftime('%m/%d/%Y %H:%M')"]
    d-->e["saldo = int(obtener_saldo(dni))"]
    e-->f["monto = int(monto)"]
    f-->g{"movimiento=='1'"}
    g-->|si|h["movimiento = "deposito""]
    h-->i["saldo = saldo + monto"]
    i-->z["linea = [fecha_hora, movimiento, saldo, monto]"]
    g-->|sino|j{"movimiento =='2'"}
    j-->|si|k{monto>saldo:}
    k-->|si|l[raise saldo_insuficiente_exception]
    k-->|no|m["movimiento='extraccion'"]
    m-->n["saldo=saldo-monto"]
    l-->z
    n-->z
    j-->|sino|p{movimiento=='3'}
    p-->|si|q{"monto>saldo:"}
    q-->|si|r[raise saldo_insuficiente_exception]
    q-->|no|s["movimiento = 'transferencia'"]
    s-->t["saldo = saldo - monto"]
    r-->z
    t-->z
    z-->u["with open(ruta, 'a') as archivo:"]
    u-->v["escritor = csv.writer(archivo)"]
    v-->w["escritor.writerow(linea)"]
    w-->x((fin))
```

Grafo de complejidad ciclomatica de la función MODIFICAR_SALDO del apartado funciones:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
    f-->|VI|g((7))
    g-->|si-VII|h((8))
    h-->|VIII|i((9))
    i-->|IX|z((10))
    g-->|sino-XIV|j((15))
    j-->|si-XV|k((16))
    k-->|si-XVI|l((17))
    k-->|no-XVIII|m((18))
    m-->|XIX|n((19))
    l-->|VII|z
    n-->|XX|z
    j-->|sino-XXI|p((20))
    p-->|si-XXII|q((21))
    q-->|si-XXIII|r((22))
    q-->|no-XXV|s((23))
    s-->|XXVI|t((24))
    r-->|XXIV|z
    t-->|XXVII|z
    z-->|X|u((11))
    u-->|XI|v((12))
    v-->|XII|w((13))
    w-->|XIII|x((14))
    
style g fill:#909    
style j fill:#909 
style k fill:#909 
style p fill:#909 
style q fill:#909 
```
Calculos complejidad cilomatica función MODIFICAR_SALDO del apartado funciones:

-V(G)=Regiones=5.\
-V(G)=A-N+2=27-24+2=5.\
-V(G)=P+1=4+1=5.

Caminos posibles función MODIFICAR_SALDO del apartado funciones:

-1-2-3-4-5-6-7-8-9-10-11-12-13-14.\
-1-2-3-4-5-6-7-15-16-17-10-11-12-13-14.\
-1-2-3-4-5-6-7-15-16-18-19-10-11-12-13-14.\
-1-2-3-4-5-6-7-15-20-21-22-10-11-12-13-14.\
-1-2-3-4-5-6-7-15-20-21-23-24-10-11-12-13-14.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función QUIERE_IMPRIMIR_TICKET del apartado mensajes:

```mermaid
graph
    a((inicio))-->b["opcion =' '"]
    b-->c["while opcion != 's' and opcion != 'n': "]
    c-->d["opcion = input('Quiere imprimir el ticket: s/n -> ')"]
    d-->e["opcion = opcion.lower()"]
    e-->c
    c-->f["resultado = False"]
    f-->g{"opcion=='s'"}
    g-->|si|h[resultado=True]
    h-->i(fin-return resultado)
    g-->i
```
Grafo de complejidad ciclomatica de la función QUIERE_IMPRIMIR_TICKET del apartado mensajes:

```mermaid
graph
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|c
    c-->|VI|f((6))
    f-->|VII|g((7))
    g-->|si-VIII|h((8))
    h-->|IX|i((9))
    g-->|X|i

style c fill:#909 
style g fill:#909 
```
Calculos complejidad cilomatica función QUIERE_IMPRIMIR_TICKET del apartado funciones:

-V(G)=Regiones=3.\
-V(G)=A-N+2=10-9+2=3.\
-V(G)=P+1=2+1=3.

Caminos posibles función QUIERE_IMPRIMIR_TICKET del apartado funciones:

-1-2-3-4-5-3-6-7-8-9.\
-1-2-3-4-5-3-6-7-9.\
-1-2-3-6-7-9.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Diagrama de flujo de la función TRANSFERENCIAS del apartado mensajes:

```mermaid
graph 
    a((inicio))-->b["funciones.modificar_saldo(dni, '3', monto)"]
    b-->c["saldo = funciones.obtener_saldo(dni)"]
    c-->d["ticket = funciones.formatear_ticket(f'Transfirió {monto}\n', f'A la cuenta: {destino}')"]
    d-->e("print(ticket)")
    e-->f(fin - return ticket)
```

Grafo de complejidad ciclomatica de la función TRANSFERENCIAS del apartado mensajes:

```mermaid
graph 
    a((1))-->|I|b((2))
    b-->|II|c((3))
    c-->|III|d((4))
    d-->|IV|e((5))
    e-->|V|f((6))
```

Calculos complejidad cilomatica función TRANSFERENCIAS del apartado funciones:

-V(G)=Regiones=1.\
-V(G)=A-N+2=5-6+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función TRANSFERENCIAS del apartado funciones:

-1-2-3-4-5-6.
