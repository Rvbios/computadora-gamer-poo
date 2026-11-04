# Sistema de Computadoras Gamer (Avance 2 de POO)
# Modela PCs gamer de escritorio y portátiles. Amplía la clase ComputadoraGamer
# del Avance 1 con encapsulamiento, herencia y polimorfismo.


# Creación de la clase base
class ComputadoraGamer:
    def __init__(self, marca, procesador, memoria_ram, tarjeta_grafica):
        self.marca = marca
        self.procesador = procesador
        # Esta asignación pasa por el setter, así que la RAM se valida desde el inicio
        self.memoria_ram = memoria_ram
        self.tarjeta_grafica = tarjeta_grafica

    # Aplicación de Encapsulamiento: __memoria_ram es privado.
    # El getter permite consultar el valor sin exponer el atributo.
    @property
    def memoria_ram(self):
        return self.__memoria_ram

    # El setter solo acepta enteros positivos, para proteger la integridad del dato
    @memoria_ram.setter
    def memoria_ram(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError(f"RAM inválida: {valor}. Debe ser un entero mayor que 0.")
        self.__memoria_ram = valor

    # Métodos operativos de la clase base
    def encender(self):
        print(f"La {self.marca} se está encendiendo, tiene un {self.procesador}")

    def jugar(self, juego):
        print(f"La {self.marca} está corriendo {juego} usando su {self.tarjeta_grafica}")

    def actualizar_ram(self, ram_nueva):
        ram_anterior = self.memoria_ram
        # Si el valor no es válido, el setter lanza ValueError y la RAM no cambia
        self.memoria_ram = ram_nueva
        print(f"Se actualizó la RAM de la {self.marca}: de {ram_anterior}GB a {ram_nueva}GB")

    def cambiar_tarjeta_grafica(self, nueva_tarjeta):
        print(f"Se cambió la tarjeta gráfica de la {self.marca}: de {self.tarjeta_grafica} a {nueva_tarjeta}")
        self.tarjeta_grafica = nueva_tarjeta

    # Este método se sobrescribe en la subclase (Polimorfismo)
    def describir(self):
        return f"PC de escritorio {self.marca} | {self.procesador} | {self.memoria_ram}GB RAM | {self.tarjeta_grafica}"


# Creación de la subclase: una portátil también es una ComputadoraGamer
class ComputadoraGamerPortatil(ComputadoraGamer):
    # Porcentaje de batería que consume cada sesión de juego
    CONSUMO_POR_PARTIDA = 40

    # Uso de super() y Herencia: la clase base inicializa los atributos comunes
    def __init__(self, marca, procesador, memoria_ram, tarjeta_grafica, duracion_bateria, peso_kg):
        super().__init__(marca, procesador, memoria_ram, tarjeta_grafica)
        # Atributos nuevos, propios de la subclase
        self.duracion_bateria = duracion_bateria
        self.peso_kg = peso_kg
        # Atributo protegido: la batería solo cambia al jugar o al cargar
        self._porcentaje_bateria = 100

    # Getter de solo lectura: no hay setter, así que no se asigna desde fuera
    @property
    def porcentaje_bateria(self):
        return self._porcentaje_bateria

    # Sobrescritura de métodos (Polimorfismo): extiende el método de la clase base
    def encender(self):
        super().encender()
        print(f"Funciona con batería: {self.porcentaje_bateria}% disponible")

    # Sobrescritura de métodos (Polimorfismo): agrega el consumo de batería
    def jugar(self, juego):
        if self._porcentaje_bateria < self.CONSUMO_POR_PARTIDA:
            print(f"La {self.marca} no puede correr {juego}: solo tiene {self.porcentaje_bateria}% de batería")
            return
        super().jugar(juego)
        self._porcentaje_bateria -= self.CONSUMO_POR_PARTIDA
        print(f"Batería restante de la {self.marca}: {self.porcentaje_bateria}%")

    # Sobrescritura de métodos (Polimorfismo): da una descripción distinta
    def describir(self):
        return (
            f"Portátil {self.marca} | {self.procesador} | {self.memoria_ram}GB RAM | {self.tarjeta_grafica} | "
            f"Batería: {self.duracion_bateria}h | Peso: {self.peso_kg}kg"
        )

    # Método propio de la subclase
    def cargar_bateria(self):
        self._porcentaje_bateria = 100
        print(f"La {self.marca} terminó de cargar: {self.porcentaje_bateria}% de batería")


# Instanciación y pruebas: 1 objeto de la clase base y 2 de la subclase
pc1 = ComputadoraGamerPortatil("ASUS ROG", "Intel i7", 16, "RTX 3060", 5, 2.3)
pc2 = ComputadoraGamer("Alienware", "AMD Ryzen 7", 32, "RTX 4070")
pc3 = ComputadoraGamerPortatil("HP Omen", "Intel i5", 8, "GTX 1660", 4, 2.5)

# Prueba de Herencia: pc1 y pc3 usan métodos heredados de la clase base.
# encender() y jugar() ejecutan la versión sobrescrita en las portátiles.
print("ASUS ROG")
pc1.encender()
pc1.jugar("Valorant")
pc1.actualizar_ram(32)

print("\n Alienware ")
pc2.encender()
pc2.jugar("Cyberpunk 2077")

print("\n HP Omen ")
pc3.encender()
pc3.cambiar_tarjeta_grafica("RTX 2060")
pc3.jugar("Minecraft")

# Prueba de Encapsulamiento: consulta y cambio controlado de la RAM
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

# Prueba de Polimorfismo: la misma llamada ejecuta el método de cada clase
print("\n Polimorfismo ")
for computadora in (pc1, pc2, pc3):
    print(computadora.describir())

# Prueba del método propio y de la restricción de batería
print("\n Batería de la portátil ")
pc1.jugar("Cyberpunk 2077")
pc1.jugar("Minecraft")
pc1.cargar_bateria()

# Prueba de independencia: cada objeto guarda sus datos en su propio self
print("\n Cada computadora guarda su propia información (su propio self) ")
print(f"{pc1.marca} tiene {pc1.memoria_ram}GB de RAM y {pc1.tarjeta_grafica}")
print(f"{pc2.marca} tiene {pc2.memoria_ram}GB de RAM y {pc2.tarjeta_grafica}")
print(f"{pc3.marca} tiene {pc3.memoria_ram}GB de RAM y {pc3.tarjeta_grafica}")
print(f"Batería de {pc1.marca}: {pc1.porcentaje_bateria}% | Batería de {pc3.marca}: {pc3.porcentaje_bateria}%")
