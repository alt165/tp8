Diagrama de flujo función EXTRACCIONES. 

```mermaid
graph
    A([Inicio]) --> B(saldo=funciones.seleccionar_moneda) 
    B --> C(intento=0)
    C --> D[while intento < 2]
    D --> E[/"monto=int(input('Ingrese el monto a retirar'))"/]
    E --> F(intento+=1)
    F --> G{monto <= saldo}
    G --> |si| H[cliente.saldo-=monto]
    H --> I(intento+=1)
    I --> J("print('Retire su dinero')")
    G --> |no| K{monto>saldo}
    K --> |si| L("print('No posse saldo suficiente')")
    L --> M{intento < 2}
    M --> |si| N("print('1.Modificar monto.  2.Volver al menu')")
    N --> O[/"eleccion=input()"/]
    O --> P{eleccion=='2'}
    P --> |si| Q[intento+=1]
    Q --> R((Fin))
    M --> R
    J --> R
    P --> |no| D
  ```

Grafo de complejidad función EXTRACCIONES.

```mermaid
graph 
    Nombre[Grafo de complejidad ciclomatica EXTRACCIONES]
    A((1)) --> |I| B((2))
    B --> |II|C((3))
    C --> |III|D((4))
    D --> |IV| E((5))
    E --> |V|F((6))
    F --> |VI|G((7))
    G --> |si - VII| H((8))
    H -->|VIII| I((9))
    I -->|IX| J((10))
    G --> |no - XI| K((12))
    K --> |si - XII| L((13))
    L --> |XIII|M((14))
    M --> |si - XIV| N((15))
    N --> |XV|O((16))
    O --> |XVI|P((16))
    P --> |si- XVII| Q((17))
    Q --> |XVIII|R((11))
    M --> |XIX|R
    J -->|X| R
    P --> |no- XX| D
```  

Calculos complejidad cilomatica función EXTRACCIONES:

-V(G)=Regiones=4.\
-V(G)=A-N+2=20-18+2=4.\
-V(G)=P+1=3+1=4.

Caminos posibles función EXTRACCIONES:

-1-2-3-4-5-6-7-8-9-10-11\
-1-2-3-4-5-6-7-12-13-14-15-16-17-18-11\
-1-2-3-4-5-6-7-12-13-14-11\
-1-2-3-4-5-6-7-12-13-14-15-16-17-4-5-6-7-12-13-14-11

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
    G-->I["cliente_encontrado=cliente(coincidencia[0],(coincidencia[1],(coincidencia[2],(coincidencia[3])"]
    I-->H((FIN - return))
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
    G-->|VII|I((8))
    I-->|VIII|H((9))

style F fill:#909
```
Calculos complejidad cilomatica función CLIENTES:

-V(G)=Regiones=1.\
-V(G)=A-N+2=9-9+2=1.\
-V(G)=P+1=0+1=1.

Caminos posibles función CLIENTES:

-1-2-3-4-5-6-7-8-9

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
-1-2-3-4-5-6-7
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
i-->k[while largo<0:]
j-->k
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
h-->|no-XIII|j((13))
i-->|VIII|k((9))
j-->|XIV|k
k-->|IX|l((10))
l-->|X|m((11))
m-->|XI|k
k-->|XII|n((12))

style h fill:#909
style k fill:#909
```

Calculos complejidad cilomatica función ULTIMOS_MOVIMIENTOS:

-V(G)=Regiones=3.\
-V(G)=A-N+2=14-12+2=4.\
-V(G)=P+1=2+1=3

Caminos posibles función ULTIMOS_MOVIMIENTOS:
-1-2-3-4-5-6-7-8-9-10-11-12
-1-2-3-4-5-6-7-12-9-10-11-12
-1-2-3-4-5-6-7-8-9-10-11-9-10-11-9-12

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

