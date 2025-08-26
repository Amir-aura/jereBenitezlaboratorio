def Ejercicio1():
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for fila in matriz1:
        print(fila)
def Ejercicio2():
    matriz2 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    suma_total = 0
    for fila in matriz2:
        for num in fila:
            suma_total += num
    for fila in matriz2:
        print(fila)
    print("Suma total:", suma_total)
def Ejercicio3():
    matriz3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    for fila in matriz3:
        print(fila)

    fila_usuario = int(input("ingrese el índice de fila 0-3: "))
    columna_usuario = int(input("ingrese el índice de columna 0-3: "))

    print("Elemento en ese índice:", matriz3[fila_usuario][columna_usuario])
def Ejercicio4():
    matriz4 = [
        [12, 45, 78, 34],
        [89, 23, 56, 90],
        [67, 44, 11, 5],
        [9, 100, 32, 76]
    ]
    maximo = matriz4[0][0]
    for fila in matriz4:
        for num in fila:
            if num > maximo:
                maximo = num
    for fila in matriz4:
        print(fila)
    print("Número más grande de la matriz:", maximo)
