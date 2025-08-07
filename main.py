def Ejercicio1():
    try:
        num1 = int(input("ingrese el primer número entero: "))
        num2 = int(input("ingrese el segundo numero entero: "))
        resultado = num1 / num2
        print(f"el resultado de la division es:",resultado)
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
def Ejercicio2():
   x = True
   while x:
        try:
            edad = int(input("ingrese su edad: "))
            print("Tu edad es: ",edad)
            x = False
        except ValueError:
            print("Eso no es un numero brutoo, elegí otro")
            x = True
def Ejercicio3():
    nombres = ["Ana", "Pedro", "Sofía"]
    try:
        indice = int(input("Ingresá un número de índice (1 a 3): "))
        print("Nombre en ese índice:", nombres[indice -1])
    except IndexError:
        print("Índice fuera del rango. Solo hay 3 nombres Sybau.")
def Ejercicio4():
    try:
        num1 = int(input("Ingresá el primer número: "))
        num2 = int(input("Ingresá el segundo número: "))
        resultado = num1 + num2
        print("La suma es:", resultado)
    except (ValueError, TypeError):
        print("Ocurrió un error, ingresar solo números enteros.")
def Ejercicio5():
    try:
        num1 = int(input("Ingresá el primer número: "))
        num2 = int(input("Ingresá el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("¡No se puede dividir por cero! BURROO")
    except ValueError:
        print("intento inválido, ingresar solo números.")
    finally:
        print("Fin del programa.")
