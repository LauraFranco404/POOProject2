class Animal:
    def __init__(self, id, nombre, edad, especie, tipoA, horasS, tiempoJuego, estadoSalud, habitat):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.tipoA = tipoA
        self.horasS = horasS
        self.tiempoJuego = tiempoJuego
        self.estadoSalud = estadoSalud
        self.habitat = habitat
        self.estaJugando = "No ha jugado"
        self.haDormido = "No ha dormido"

    def mostrarAnimal(self):
        print("Animal: ", self.id, self.nombre, self.edad, self.especie, self.tipoA, self.horasS, self.tiempoJuego, self.estadoSalud, self. habitat, self.estaJugando)
