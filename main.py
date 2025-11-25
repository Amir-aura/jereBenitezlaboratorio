def suma_esquinas():
    matriz =[[1, 5, 3, 5],
             [8, 5, 9, 2],
             [4, 5, 6, 7],
             [1, 2, 3, 4]]
    sumaEsquinas=0
    n=len(matriz)
    sumaEsquinas+=matriz[0][0]
    sumaEsquinas += matriz[0][n-1]
    sumaEsquinas += matriz[n-1][n-1]
    sumaEsquinas += matriz[n-1][0]
    print(sumaEsquinas)

def diagonal_principal():
    matriz = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
    y=0
    y2=2
    sumaDiagonal1=0
    sumaDiagonal2=0
    for x in range(len(matriz)):
        sumaDiagonal1+=matriz[x][y]
        sumaDiagonal2+=matriz[x][y2]
        y+=1
        y2-=1
    print(sumaDiagonal1,sumaDiagonal2)

def identidad():
    tamaño=int(input("ingrese la dimencion de la matriz identidad: "))
    matriz=[]
    for x in range(tamaño):
        fila_nueva=[]
        for y in range(tamaño):
            if x==y:
                fila_nueva.append(1)
            else:
                fila_nueva.append(0)
        matriz.append(fila_nueva)
    for x in matriz:
        print(x)