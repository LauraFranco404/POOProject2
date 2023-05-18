class Habitat:
    def __init__(self, id, nombreH, temperaturaH, tipoAH, disponibilidad):
        self.id = id
        self.nombreH = nombreH
        self.temperaturaH = temperaturaH
        self.tipoAH = tipoAH
        self.disponibilidad = disponibilidad
        self.animales = []

    def mostrarHabitat(self):
        print(self.id, "Habitat", self.nombreH)
        print("Temperatura:", self.temperaturaH)
        print("Tipo de alimentación en el habitat:", self.tipoAH)
        print("Disponibilidad para animales:", self.disponibilidad)
        if len(self.animales) > 0:
            print(self.listarAnimales())
        else:
            print("Aún no hay animales disponibles :c")

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def listarAnimales(self):
        print("Lista de animales: ")
        for animal in self.animales:
            animal.mostrarAnimal()

    def liberarAnimal(self, id):
        for i, animal in enumerate(self.animales):
            if animal.id == id:
                self.animales.pop(i)

    def accederAnimal(self, id):
        for i, animal in enumerate(self.animales):
            if animal.id == id:
                return animal
            else:
                print("Lo siento, este id no pertenece a ningún animal")
