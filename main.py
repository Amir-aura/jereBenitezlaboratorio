def Ejercicio1_2_6():
    informacion={
            "Nombre":"CHARLIE",
            "Apellido" : "KIRK",
            "Edad":16,
            "Ciudad":"NY",
            "Profecion":"Racista"
        }
    print(f"""
            Nombre: {informacion["Nombre"]}
            Apellido: {informacion['Apellido']}
            Edad: {informacion['Edad']}
            Ciudad: {informacion['Ciudad']}
            Profecion: {informacion['Profecion']}
            """)
    #Ejercicio 2

    informacion["Telefono"]=1125477005
    informacion["Email"]="Charlie.Kirk67@gmail.com"
    print(f"""
            Nombre: {informacion["Nombre"]}
            Apellido: {informacion['Apellido']}
            Edad: {informacion['Edad']}
            Ciudad: {informacion['Ciudad']}
            Profecion: {informacion['Profecion']}
            Telefono: {informacion['Telefono']}
            Email: {informacion['Email']}
            """)
    #Ejercicio6
    del informacion["Telefono"]
    print(f"""
            Nombre: {informacion["Nombre"]}
            Apellido: {informacion['Apellido']}
            Edad: {informacion['Edad']}
            Ciudad: {informacion['Ciudad']}
            Profecion: {informacion['Profecion']}
            Email: {informacion['Email']}
            """)

def ejercicio3y4():
    Notas={
            "Lengua":8,
            "Ingles":9,
            "Laboratorio":10,
            "Base de datos":8,
            "proyecto":10,
        }
    asignatura=input("ingrese la asigntura que desea revisar con la primera letra en Mayuscula: ")
    print(Notas[asignatura])
    promedio=0
    cantidad=len(Notas)
    for nota in Notas:
        promedio+=Notas[nota]
    promedio/=cantidad
    print(f"el promedio es:{promedio}")

def capitales_pais():
    paises = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción",
        "España": "Madrid",
        "Francia": "París",
        "Italia": "Roma"
    }
    pais = input("Ingrese un país: ")
    capital = paises[pais]
    if capital:
        print(f"La capital de {pais} es {capital}.")
    else:
        print("Ese país no está" )

def calcular_costo():
    precios = {
        "pan": 300,
        "leche": 500,
        "queso": 1200,
        "huevos": 900,
        "azúcar": 700,
        "arroz": 800
    }
    producto=input("ingrese el producto a comprar: ")
    cantidad=int(input("ingrese la cantidad deseada"))
    if producto in precios:
        total = precios[producto] * cantidad
        print(f"El costo total de {cantidad} {producto}(s) es ${total}.")
    else:
        print("El producto no está en la tienda.")