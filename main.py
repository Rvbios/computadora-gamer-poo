# Sistema de Computadoras Gamer (Avance 3 de POO)
# Archivo principal: solo importaciones, creación de objetos y pruebas.
from modelos import TarjetaGrafica, Bateria, ComputadoraGamer, ComputadoraGamerPortatil

# Componentes (objetos que se usan por Composición)
rtx3060 = TarjetaGrafica("RTX 3060", 12)
rtx4070 = TarjetaGrafica("RTX 4070", 12)
gtx1660 = TarjetaGrafica("GTX 1660", 6)

# Instanciación: 1 objeto de la clase base y 2 de la subclase
pc1 = ComputadoraGamerPortatil("ASUS ROG", "Intel i7", 16, rtx3060, Bateria(5), 2.3)
pc2 = ComputadoraGamer("Alienware", "AMD Ryzen 7", 32, rtx4070)
pc3 = ComputadoraGamerPortatil("HP Omen", "Intel i5", 8, gtx1660, Bateria(4), 2.5)

# Herencia: pc1 y pc3 usan métodos heredados de la clase base.
# encender() y jugar() ejecutan la versión sobrescrita en las portátiles.
print(" ASUS ROG ")
pc1.encender()
pc1.jugar("Valorant")
pc1.actualizar_ram(32)

print("\n Alienware ")
pc2.encender()
pc2.jugar("Cyberpunk 2077")

print("\n HP Omen ")
pc3.encender()
pc3.cambiar_tarjeta_grafica(TarjetaGrafica("RTX 2060", 6))
pc3.jugar("Minecraft")

# Composición: métodos del objeto contenido invocados a través del contenedor
print("\n Composición ")
print(f"Tarjeta de {pc2.marca}: {pc2.tarjeta_grafica}")
print(pc2.tarjeta_grafica.renderizar("Fortnite"))
print(f"Duración de batería de {pc1.marca}: {pc1.bateria.duracion_horas}h")

# Encapsulamiento: consulta y cambio controlado de la RAM
print("\n Encapsulamiento ")
print(f"RAM de {pc2.marca} consultada con el getter: {pc2.memoria_ram}GB")

# El setter rechaza valores no válidos y la RAM conserva su valor
for valor_invalido in (-8, 0, "mucha"):
    try:
        pc2.memoria_ram = valor_invalido
    except ValueError as error:
        print(f"Error controlado: {error}")
print(f"La RAM de {pc2.marca} sigue en {pc2.memoria_ram}GB")

# El atributo privado no se puede leer directamente desde fuera de la clase
try:
    print(pc2.__memoria_ram)
except AttributeError:
    print("No se puede leer __memoria_ram desde fuera: es un atributo privado")

# Polimorfismo: la misma llamada ejecuta el método de cada clase
print("\n Polimorfismo ")
for computadora in (pc1, pc2, pc3):
    print(computadora.describir())

# Método propio de la subclase y restricción de batería
print("\n Batería de la portátil ")
pc1.jugar("Cyberpunk 2077")
pc1.jugar("Minecraft")
pc1.cargar_bateria()

# Independencia: cada objeto guarda sus propios componentes
print("\n Cada computadora guarda su propia información ")
for computadora in (pc1, pc2, pc3):
    print(f"{computadora.marca} tiene {computadora.memoria_ram}GB de RAM y {computadora.tarjeta_grafica}")
print(f"Batería de {pc1.marca}: {pc1.porcentaje_bateria}% | Batería de {pc3.marca}: {pc3.porcentaje_bateria}%")
