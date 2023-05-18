class Alimento:
    def __init__(self, id, nombre, tipoA):
        self.id = id
        self.nombre = nombre
        self.tipoA = tipoA

    def mostrarAlimento(self):
        print("Alimento: ", self.id, self.nombre, self.tipoA)
