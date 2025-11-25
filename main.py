import random
matriz=[["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""]]
matrizAmostrar=[["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""]]
cofres=3
for x in range(cofres):
        indice1 = random.randint(0,9)
        indice2 = random.randint(0,9)
        matriz[indice1][indice2]="✓"
intentos=5

while cofres>0 and intentos!=0:
        print(f"te quedan {intentos} intentos")
        for fila in matrizAmostrar:
                print(fila)
        valor1=int(input("ingrese la fila en donde cree que esta: "))
        valor2 = int(input("ingrese la columna en donde cree que esta: "))
        if matriz[valor1-1][valor2-1]=="✓":
                matrizAmostrar[valor1-1][valor2-1]="✓"
                cofres -= 1
                print(f"le diste te quedan {cofres} Cofres")
        else:
                matrizAmostrar[valor1-1][valor2-1] = "X"
                print(f"no le diste intentalo devuelta te quedan {cofres} cofres")
                intentos-=1

if intentos==0:
        print(f"""perdiste Nword 
                el mapa con los cofres era:
""")
        for fila in matriz:
                print(fila)
else:
        print("ganaste🙄")