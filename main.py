productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}]

def ejercicio1():
    for producto in productos:
            print(producto["nombre"])
def ejercicio2():
    sumaTotal= 0
    for producto in productos:
        sumaTotal += producto["precio"]
    print("La suma total del precio es:",sumaTotal)

def ejercicio3():
    nuevoproducto = {"nombre": "Monitor", "precio": 300, "categoria": "Electrónica"}
    productos.append(nuevoproducto)
    print("la lista con los nuevos productos son:")
    for producto in productos:
            print(producto["nombre"])
def ejercicio4():
    indice = int(input("ingrese la posicion del producto al que desea cambiar el precio: "))
    nuevoprecio=int(input("Ingrse el nuevo precio: "))
    productos[indice]["precio"]= nuevoprecio
    print(productos[indice-1])

#----------------------------------------------------------------------------------------------#

estudiantes = [
    {"nombre": "Ana", "edad": 21, "calificacion": 90},
    {"nombre": "Luis", "edad": 22, "calificacion": 95},
    {"nombre": "Marta", "edad": 20, "calificacion": 85}
]

def ejrecicio5():
    estudiantemejornota = estudiantes[0]
    for estudiante in estudiantes[1:]:
        if estudiante["calificacion"] > estudiantemejornota["calificacion"]:
            estudiante_mejor_nota = estudiante
    print("Estudiante con la calificación más alta:",estudiante_mejor_nota)

def ejercicio6():
    nombresestudiantes=[]
    for estudiante in estudiantes:
        nombresestudiantes.append(estudiante["nombre"])
    print("Lista con los nombres de los estudiantes:", nombresestudiantes)
#-----------------------------------------------------------------------------------------------

libros = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
]
def ejercicio7():
    libro=libros[1]
    print(libros)
    libros.pop(1)
    print(libros)
    libros.append(libro)
    print(libros)
def ejercicio8():
    for libro in libros:
        libro["disponible"]=True
        print(libro)