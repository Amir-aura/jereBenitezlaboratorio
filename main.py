def crear_Arreglo():
    cantidad_elementos = int(input("cuantos elementos tendra el arreglo? "))
    arreglo = []
    for x in range(cantidad_elementos):
        elemento = int(input(f"ingrese el elemento {x + 1}: "))
        arreglo.append(elemento)
    return arreglo


def busqueda_Secuencial(buscar):
    try:
        valor_a_buscar = buscar
        for i in range(len(Arreglo)):
            if Arreglo[i] == valor_a_buscar:
                return i
        return -1
    except NameError:
        print("no se a encontrado ningun arreglo")


def ordenamiento_Seleccion():
    try:
        indice = len(Arreglo)
        for i in range(indice):
            minimo = i
            for j in range(i + 1, n):
                if Arreglo[j] < Arreglo[minimo]:
                    minimo = j
            Arreglo[i], Arreglo[minimo] = Arreglo[minimo], Arreglo[i]
            print(Arreglo)
        return Arreglo
    except NameError:
        print("no se a encontrado ningun arreglo")


def ordenamiento_Insercion():
    try:
        for i in range(1, len(Arreglo)):
            key = Arreglo[i]
            j = i - 1
            while j >= 0 and key < Arreglo[j]:
                Arreglo[j + 1] = Arreglo[j]
                j -= 1
                print(Arreglo)
            Arreglo[j + 1] = key
        return Arreglo
    except NameError:
        print("no se a encontrado ningun arreglo")


def ordenamiento_Burbuja():
    try:
        n = len(Arreglo)
        for i in range(n - 1):
            Hay_Cambio = False
            for j in range(0, n - i - 1):
                if Arreglo[j] > Arreglo[j + 1]:
                    Arreglo[j], Arreglo[j + 1] = Arreglo[j + 1], Arreglo[j]
                    Hay_Cambio = True
                    print(Arreglo)
            if not Hay_Cambio:
                break
        return Arreglo
    except NameError:
        print("no se a encontrado ningun arreglo")


def busqueda_Binaria(buscar):
    try:
        ordenado = int(input("la lista esta ordenada? (1Si/2No): "))
        valor = buscar
        if ordenado == 1:
            izquierda = 0
            derecha = len(Arreglo) - 1
            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                if Arreglo[medio] == valor:
                    print(f"el elemento {buscar} esta en la posicion {medio}")
                    break
                elif Arreglo[medio] < valor:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1
            return -1
        elif ordenado == 2:
            print("ordenala porq no se puede hacer sino")
    except NameError:
        print("no se a encontrado ningun arreglo")


while True:
    try:
        opcion = int(input("""
                  |=====================|
                  |         menu        |
                  |                     |
                  | 1) crear Arreglo    |
                  |                     |
                  | 2) ordenar          |
                  |                     |   
                  | 3) buscar           |
                  |                     |
                  | 4) salir            |
                  |                     |
                  |=====================|

                  ingrese una opcion: """
                           ))
        if opcion == 1:
            Arreglo = crear_Arreglo()
        elif opcion == 2:
            opcion = int(input("""
                  |=====================|
                  |     ordenamieto     |
                  |                     |
                  | 1) burbuja          |
                  |                     |
                  | 2) inserecion       |
                  |                     |   
                  | 3) seleccion        |
                  |                     |
                  |=====================|

                  ingrese una opcion: """
                               ))
            if opcion == 1:
                print(F"el Arreglo ordenado es: {ordenamiento_Burbuja()}")
            elif opcion == 2:
                print(F"el Arreglo ordenado es: {ordenamiento_Insercion()}")
            elif opcion == 3:
                print(F"el Arreglo ordenado es: {ordenamiento_Seleccion()}")
            else:
                print("al menu principal por bobo")
        elif opcion == 3:
            opcion = int(input("""
                  |=====================|
                  |       busqueda      |
                  |                     |
                  | 1) Binaria          |
                  |                     |
                  | 2) Secuencial       |
                  |                     |
                  |=====================|

                  ingrese una opcion: """
                               ))
            buscar = int(input("ingrese el elemento a buscar: "))
            if opcion == 1:
                indice = busqueda_Binaria(buscar)
                print(F"el elemento {buscar} esta en la posicion: {indice}")
            elif opcion == 2:
                indice = busqueda_Secuencial(buscar)
                print(F"el elemento {buscar} esta en la posicion: {indice}")
            else:
                print("al menu principal por bobo")
        elif opcion == 4:
            print("saliendo...")
            break
        else:
            pass
    except ValueError:
        print("Ingrese un valor válida.")