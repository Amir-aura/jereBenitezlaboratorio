def Ejercicio1():
    numeros = []
    for i in range(5):
        num = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)
    print("Los números ingresados son:")
    for numero in numeros:
        print(numero)
def Ejercicio2():
    frutas = ["manzana", "banana", "uva", "naranja", "mandarina"]
    buscar = input("Ingrese el nombre de una fruta: ").lower()
    if buscar in frutas:
        print(f"La fruta '{buscar}' está en la posición",frutas.index(buscar))
    else:
        print(f"La fruta '{buscar}' no fue encontrada.")
def Ejercicio3():
    notas = []
    for X in range(10):
        nota = float(input(f"Ingrese la nota del estudiante {X + 1}: "))
        notas.append(nota)
    suma_total = sum(notas)
    promedio = suma_total / len(notas)
    print("Suma total de las notas:", suma_total)
    print("Promedio de las notas:", promedio)
def Ejercicio4():
    temperaturas = [22, 25, 19, 30, 28, 21, 24]
    maximo = temperaturas[0]
    minimo = temperaturas[0]

    for temp in temperaturas:
        if temp > maximo:
            maximo = temp
        if temp < minimo:
            minimo = temp

    print(f"Temperatura máxima: {maximo}")
    print(f"Temperatura mínima: {minimo}")
def Ejercicio5():
    numeros = [23, 5, 89, 1, 34, 12, 55]
    numeros.sort()
    print("Lista ordenada:", numeros)
def Ejercicio6():
    numeros = [12, 7, 9, 20, 15, 6, 3, 8, 11, 10, 14, 1, 4, 5, 2]
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
