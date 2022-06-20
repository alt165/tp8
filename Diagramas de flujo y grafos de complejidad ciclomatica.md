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
-V(G)=P+1=3+1=4.\

Caminos posibles función EXTRACCIONES:

-1-2-3-4-5-6-7-8-9-10-11\
-1-2-3-4-5-6-7-12-13-14-15-16-17-18-11\
-1-2-3-4-5-6-7-12-13-14-11\
-1-2-3-4-5-6-7-12-13-14-15-16-17-4-5-6-7-12-13-14-11\
