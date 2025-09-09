def mazoposible():
    posiblesPalos = ["♥", "♦", "♣", "♠"]
    mazo = []
    for palo in posiblesPalos:
        for numero in range(1, 14):
            if numero == 1:
                numero = "A"
            elif numero == 11:
                numero = "J"
            elif numero == 12:
                numero ="Q"
            elif numero == 13:
                numero = "K"
            carta = [numero, palo]
            mazo.append(carta)
    return mazo

def mazosuma():
    try:
        mazo = mazoposible()
        print("mazo:")
        promedio1= 0
        for fila in mazo:
            if fila [0] == "A":
                promedio1+= 11
            elif fila [0] == "J" or fila [0] == "Q" or fila [0] == "K":
                promedio1+= 10
            else: promedio1 += fila [0]
        for fila in mazo:
            print(fila)
        print("la suma es:",promedio1)
    except ValueError:
        print("Ingrese una opción válida.")

mazosuma()
