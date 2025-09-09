import random
def simulacro_matrices():
    posiciones = [["Arquero"],
                 ["Defensor"],
                 ["Mediocampista"],
                 ["Delantero"]]
    nombres = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kylian Mbappé",
    "Erling Haaland",
    "Neymar Jr.",
    "Kevin De Bruyne",
    "Robert Lewandowski",
    "Luka Modrić",
    "Karim Benzema",
    "Mohamed Salah",
    "Harry Kane",
    "Vinícius Júnior",
    "Jude Bellingham",
    "Antoine Griezmann",
    "Federico Valverde",
    "Bernardo Silva",
    "João Cancelo",
    "Frenkie de Jong",
    "Pedri",
    "Jamal Musiala",
    "Bukayo Saka",
    "Phil Foden",
    "Gavi"
]
    filas = 23
    matriz23x3 = []
    for i in range(filas):
        lista_auxiliar = []
        nombre_random = random.randint(0, len(nombres)-1)
        posicion_random = random.randint(0, 3)
        valoracion_random = random.randint(50, 100)
        lista_auxiliar.append(nombres[nombre_random])
        lista_auxiliar.append(posiciones[posicion_random])
        lista_auxiliar.append(valoracion_random)
        matriz23x3.append(lista_auxiliar)
        nombres.remove(nombres[nombre_random])
    return matriz23x3

def equipos():
    equipo1 = simulacro_matrices()
    equipo2 = simulacro_matrices()
    print("equipo 1:")
    promedio1=0
    promedio2 = 0
    for fila in equipo1:
        print(fila)
        promedio1+=fila[2]
    print("equipo 2:")
    for fila in equipo2:
        print(fila)
        promedio2 += fila[2]
    promedio1/=23
    promedio2/=23
    if promedio1>promedio2:
        print("el equipo 1 tiene una mayor probabilidad")
    elif promedio1<promedio2:
        print("el equipo 2 tiene una mayor probabilidad")
    else:print("empatan")
equipos()