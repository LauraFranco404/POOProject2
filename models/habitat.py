class Habitat:
    def __init__(self, id, nombreH, temperaturaH, tipoAH, disponibilidad):
        self.id = id
        self.nombreH = nombreH
        self.temperaturaH = temperaturaH
        self.tipoAH = tipoAH
        self.disponibilidad = disponibilidad
        self.animales = []

#Esta función se encarga de tomar un objeto de tipo Animal e insertarlo a la lista de animales de un habitat
    def agregarAnimales(self, animal):
        self.animales.append(animal)
