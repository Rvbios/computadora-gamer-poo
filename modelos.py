# Sistema de Computadoras Gamer (Avance 3 de POO)
# Módulo de modelos: contiene todas las clases del sistema.
# Amplía el Avance 2 con Composición: una computadora "tiene-una" TarjetaGrafica
# y una portátil además "tiene-una" Bateria.


# --- CLASES AUXILIARES PARA COMPOSICIÓN ---

class TarjetaGrafica:
    def __init__(self, modelo, vram_gb):
        self.modelo = modelo
        self.vram_gb = vram_gb

    def renderizar(self, juego):
        return f"{self.modelo} ({self.vram_gb}GB VRAM) renderizando {juego}"

    def __str__(self):
        return f"{self.modelo} {self.vram_gb}GB"


class Bateria:
    def __init__(self, duracion_horas):
        self.duracion_horas = duracion_horas
        # Atributo protegido: el porcentaje solo cambia con consumir() o cargar()
        self._porcentaje = 100

    # Getter de solo lectura
    @property
    def porcentaje(self):
        return self._porcentaje

    # Devuelve True si había carga suficiente y la descuenta
    def consumir(self, cantidad):
        if self._porcentaje < cantidad:
            return False
        self._porcentaje -= cantidad
        return True

    def cargar(self):
        self._porcentaje = 100


# --- CLASE BASE ---

class ComputadoraGamer:
    def __init__(self, marca, procesador, memoria_ram, tarjeta_grafica):
        self.marca = marca
        self.procesador = procesador
        # Esta asignación pasa por el setter, así que la RAM se valida desde el inicio
        self.memoria_ram = memoria_ram
        # COMPOSICIÓN: una ComputadoraGamer "tiene-una" TarjetaGrafica
        self.tarjeta_grafica = tarjeta_grafica

    # Encapsulamiento: __memoria_ram es privado.
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

    def encender(self):
        print(f"La {self.marca} se está encendiendo, tiene un {self.procesador}")

    # Delegación: la computadora le pide a su tarjeta gráfica que renderice
    def jugar(self, juego):
        print(f"La {self.marca} está corriendo {juego}: {self.tarjeta_grafica.renderizar(juego)}")

    def actualizar_ram(self, ram_nueva):
        ram_anterior = self.memoria_ram
        # Si el valor no es válido, el setter lanza ValueError y la RAM no cambia
        self.memoria_ram = ram_nueva
        print(f"Se actualizó la RAM de la {self.marca}: de {ram_anterior}GB a {ram_nueva}GB")

    # Se reemplaza el objeto componente completo por otro TarjetaGrafica
    def cambiar_tarjeta_grafica(self, nueva_tarjeta):
        print(f"Se cambió la tarjeta gráfica de la {self.marca}: de {self.tarjeta_grafica} a {nueva_tarjeta}")
        self.tarjeta_grafica = nueva_tarjeta

    # Este método se sobrescribe en la subclase (Polimorfismo)
    def describir(self):
        return f"PC de escritorio {self.marca} | {self.procesador} | {self.memoria_ram}GB RAM | {self.tarjeta_grafica}"


# --- SUBCLASE ---

class ComputadoraGamerPortatil(ComputadoraGamer):
    # Porcentaje de batería que consume cada sesión de juego
    CONSUMO_POR_PARTIDA = 40

    # Herencia con super(): la clase base inicializa los atributos comunes
    def __init__(self, marca, procesador, memoria_ram, tarjeta_grafica, bateria, peso_kg):
        super().__init__(marca, procesador, memoria_ram, tarjeta_grafica)
        # COMPOSICIÓN: una portátil "tiene-una" Bateria
        self.bateria = bateria
        self.peso_kg = peso_kg

    # Delegación: el porcentaje se consulta a la batería
    @property
    def porcentaje_bateria(self):
        return self.bateria.porcentaje

    # Polimorfismo: extiende el método de la clase base
    def encender(self):
        super().encender()
        print(f"Funciona con batería: {self.porcentaje_bateria}% disponible")

    # Polimorfismo: agrega el consumo de batería, delegado al objeto Bateria
    def jugar(self, juego):
        if not self.bateria.consumir(self.CONSUMO_POR_PARTIDA):
            print(f"La {self.marca} no puede correr {juego}: solo tiene {self.porcentaje_bateria}% de batería")
            return
        super().jugar(juego)
        print(f"Batería restante de la {self.marca}: {self.porcentaje_bateria}%")

    # Polimorfismo: da una descripción distinta
    def describir(self):
        return (
            f"Portátil {self.marca} | {self.procesador} | {self.memoria_ram}GB RAM | {self.tarjeta_grafica} | "
            f"Batería: {self.bateria.duracion_horas}h | Peso: {self.peso_kg}kg"
        )

    # Método propio de la subclase, delegado a la batería
    def cargar_bateria(self):
        self.bateria.cargar()
        print(f"La {self.marca} terminó de cargar: {self.porcentaje_bateria}% de batería")
