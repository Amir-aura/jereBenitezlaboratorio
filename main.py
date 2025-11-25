def suma_todo():
    matriz = [[10,20,30],
              [40,50,60],
              [70,80,90]]
    filasSumadas = []
    columnasSumadas = []
    for x in range(len(matriz)):
        sumafilas = 0
        sumaColumna=0
        for y in range(len(matriz[x])):
            sumafilas+=matriz[x][y]
            sumaColumna+=matriz[y][x]
        filasSumadas.append(sumafilas)
        columnasSumadas.append(sumaColumna)
    print(filasSumadas)
    print(columnasSumadas)

def transpuesta():
    matriz = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

    transpuesta=[]
    for x in range(len(matriz)):
        filaTranpuesta= []
        for y in range (len(matriz[x])):
            filaTranpuesta.append(matriz[y][x])
        transpuesta.append(filaTranpuesta)
    for x in transpuesta:
        print(x)

def buscador():
    matriz=[[1, 5, 3, 5],
            [8, 5, 9, 2],
            [4, 5, 6, 7]]
    numero_buscar=int(input("ingrese el numero que desea buscar: "))
    apariciones=0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if numero_buscar == matriz[x][y]:
                apariciones+=1

    print(f"el numero {numero_buscar} aparece un total de {apariciones} vaces")

def promedio():
    matriz=[[1, 5, 3, 5],
            [8, 5, 9, 2],
            [4, 5, 6, 7]]
    matrizNUeva=[]
    suma=0
    for x in range(len(matriz)):
        filaNueva = []
        for y in range(len(matriz[x])):
            suma+=matriz[x][y]
    promedio=suma/12
    for x in range(len(matriz)):
        filaNueva=[]
        for y in range(len(matriz[x])):
            if matriz[x][y]<promedio:
                filaNueva.append(promedio)
            else:
                filaNueva.append(matriz[x][y])
        matrizNUeva.append(filaNueva)
    for x in matrizNUeva:
        print(x)