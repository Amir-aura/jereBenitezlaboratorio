nombres = []
telefonos = []
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ").strip()
    telefono = input("Ingrese el número de teléfono: ").strip()
    nombres.append(nombre)
    telefonos.append(telefono)
    print(f"Contacto '{nombre}' agregado con éxito.")

def mostrar_contactos():
    if not nombres:
        print("No hay contactos para mostrar.")
    else:
        print("\nLista de contactos:")
        for x in range(len(nombres)):
            print(f"{x + 1}. {nombres[x]} - {telefonos[x]}")


def buscar_contacto():
    buscar = input("Ingrese el nombre del contacto a buscar: ").strip()
    if buscar in nombres:
        indice = nombres.index(buscar)
        print(f"Contacto encontrado: {nombres[indice]} - {telefonos[indice]}")
    else:
        print("Contacto no encontrado.")


def menu():
    while True:
        print("""
       ||||||||||||||||||||||||||||||||||| 
       |       -------Menu--------       |
       | 1. Agregar contacto             |
       | 2. Mostrar todos los contactos  |
       | 3. Buscar contacto por nombre   |
       | 4. Salir                        |
       |||||||||||||||||||||||||||||||||||
        """)
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            print("kill your self 🖕🖕")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
menu()

def guardar_contactos():
    with open("contactos.txt", "w", encoding="utf-8") as archivo:
        for i in range(len(nombres)):
            archivo.write(f"{nombres[i]},{telefonos[i]}\n")
guardar_contactos()