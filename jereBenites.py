def suma():
    numeros=[1,2,3,4,5,6,7,8,9,10]
    suma=0
    for x in numeros:
        suma+=x
    print(suma)
def vocales():
    cadena="programacion en python"
    cont=0
    for letra in cadena:
       if letra in "aeiouAEIOU":
           cont+=1
    print(cont)

    nro=int(input("ingrese un nro"))
    mult=0
    for x in range(1,11):
       mult=nro*x
       print(f"{nro}x{x}={mult}")

    nros=[1,2,3,4,5,6,7,8,9,10]
    pares=[x for x in nros if x%2==0]
    print(pares)
def arbolito():
    numero_filas = int(input("Proporciona el número de filas: "))
    #arbol mitad izquierda
    for fila in range(1, numero_filas + 1):
        espacios_blanco = " " * (numero_filas - fila)
        asteriscos = "*" * (fila - 1)
        print(f"{asteriscos}{espacios_blanco}")
    #arbol entero
    for fila in range(1, numero_filas + 1):
       espacios_blanco = " " * (numero_filas - fila)
       asteriscos = "*" * (2*fila - 1)
       print(f"{espacios_blanco}{asteriscos}")
    #arbol mitad derecha
    for fila in range(1, numero_filas + 1):
       espacios_blanco = " " * (numero_filas - fila)
       asteriscos = "*" * (fila - 1)
       print(f"{espacios_blanco}{asteriscos}")

