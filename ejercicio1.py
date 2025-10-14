import random
intentos = 7
palabras = ["computadora", "tecnología", "inteligencia", "aprendizaje", "innovación", "desarrollo", "programación", "aplicación", "internet", "navegador", "seguridad", "protección", "privacidad", "documento", "información", "conocimiento", "experiencia", "comunicación", "conferencia", "mensajes", "redes", "sociales", "plataforma", "contenido", "creativo", "diseño", "fotografía", "audiovisual", "sonido", "música", "canción", "película", "televisión", "noticias", "periódico", "revista", "literatura", "escritura", "lectura", "biblioteca", "historia", "geografía", "matemáticas", "ciencia", "biología", "química", "física", "astronomía", "planeta", "universo", "naturaleza", "ambiente", "ecología", "clima", "estación", "invierno", "primavera", "verano", "otoño", "montaña", "bosque", "desierto", "océano", "ciudad", "pueblo", "edificio", "arquitectura", "transporte", "automóvil", "bicicleta", "motocicleta", "avión", "barco", "viaje", "turismo", "aventura", "exploración", "cultura", "tradición", "costumbre", "festival", "celebración", "gastronomía", "restaurante", "cocina", "receta", "ingrediente", "vegetales", "frutas", "verduras", "alimentos", "nutrición", "ejercicio", "deporte", "salud", "bienestar", "felicidad", "emoción", "sentimiento", "amistad"]
palabra_elegida = random.choice(palabras)
letras_guardadas = []
letras_erradas = []
def mostrar_progreso():
    resultado = ""
    for letra in palabra_elegida:
        if letra in letras_guardadas:
            resultado += letra + ""
        else:
            resultado += "_"
    return resultado.strip()

def palabra():
    for letra in palabra_elegida:
        if letra not in letras_guardadas:
            return False
    return True

print("\nVamos a jugar al ahorcado, tenés 7 intentos para adivinar. ")

while intentos > 0:
    print("\nProgreso de la palabra: ", mostrar_progreso())
    print(f"Intentos restantes: {intentos}")
    print(f"Letras erradas:", ", ".join(letras_erradas))
    letra_adivinada = input("Ingrese una letra: ").lower()
    if len(letra_adivinada) != 1:
        print("Ingresa una sola letra.")
    if letra_adivinada in letras_guardadas or letra_adivinada in letras_erradas:
        print("Ya tiraste esa letra.")
    if letra_adivinada in palabra_elegida:
        letras_guardadas.append(letra_adivinada)
        print("La letra está en la palabra.")
    else:
        letras_erradas.append(letra_adivinada)
        print("La letra no está en la palabra.")
        intentos -= 1
    if palabra():
        print(f"Has ganado, lcdtm, la palabra no era: {palabra_elegida.upper()}")
        break
else:
    print(f"Has perdido, la palabra era: {palabra_elegida.upper()}")

with open("palabras_jugadas.txt", "a", encoding="utf-8") as archivo:
    if intentos > 0:
        archivo.write(f"Ganada: {palabra_elegida}")
    else:
        archivo.write(f"Perdida: {palabra_elegida}")