def factorial_recursividad(NIGG):
    if NIGG <= 1:
        return 1
    else:
        return NIGG * factorial_recursividad(NIGG - 1)

numero = 5
resultado_factorial = factorial_recursividad(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")

def sumar_lista_recursivida(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumar_lista_recursivida(lista[1:])
numeros = [1, 2, 3, 4]
resultado_suma = sumar_lista_recursivida(numeros)
print(f"La suma de los elementos de {numeros} es: {resultado_suma}")

class Medicamento:
    STOCK_CRITICO_UMBRAL = 10

    def __init__(self, nombre, categoria, stock, precio, codigo_barras):
        """Inicializa un nuevo objeto Medicamento."""
        self.nombre = nombre
        self.categoria = categoria
        self.stock = int(stock)
        self.precio = float(precio)
        self.codigo_barras = codigo_barras
        print(f"Medicamento '{self.nombre}' creado con {self.stock} unidades en stock.")

    def vender(self, cantidad):

        if cantidad > self.stock:
            print(f"ERROR: No hay suficiente stock de {self.nombre}.")
            print(f"Stock actual: {self.stock}. Cantidad solicitada: {cantidad}.")
            return False
        else:
            self.stock -= cantidad
            print(f"Venta exitosa. {cantidad} unidades de {self.nombre} vendidas.")
            print(f"Nuevo stock: {self.stock}.")
            return True


    def reponer_stock(self, cantidad):
        self.stock += cantidad
        print(f" Reposición exitosa. {cantidad} unidades añadidas a {self.nombre}.")
        print(f"Nuevo stock total: {self.stock}.")


    def esta_en_stock_critico(self):
        return self.stock < self.STOCK_CRITICO_UMBRAL

ibuprofeno = Medicamento(
    nombre="ibuprofeno 500mg",
    categoria="Analgésico",
    stock=6,
    precio=6.7,
    codigo_barras="7750001000001"
)
print(f"¿Está {ibuprofeno.nombre} en stock crítico? {ibuprofeno.esta_en_stock_critico()}")
ibuprofeno.vender(cantidad=20)
ibuprofeno.vender(cantidad=8)
print(f"¿Está {ibuprofeno.nombre} en stock crítico? {ibuprofeno.esta_en_stock_critico()}")
ibuprofeno.reponer_stock(cantidad=50)
print(f"¿Está {ibuprofeno.nombre} en stock crítico? {ibuprofeno.esta_en_stock_critico()}")
