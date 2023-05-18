class Sistema:
    def __init__(self):
        self.habitats = []
        self.animales = []
        self.alimentos = []


    def agregarHabitats(self, habitat):
        self.habitats.append(habitat)
        print("El habitat ", habitat.nombreH, " ha sido agregado exitosamente")

    def accederAHabitat(self, id):
        for i, habitat in enumerate(self.habitats):
            if habitat.id == id:
                return habitat
            else:
                print("Lo siento, este id no pertenece a ningún habitat")

    def mostarHabitats(self):
        print("Listado de habitats: ")
        for habitat in self.habitats:
            habitat.mostrarHabitat()

    def agregarAlimentos(self, alimento):
        self.alimentos.append(alimento)

    def mostrarAlimentos(self):
        print("Listado de alimentos: ")
        for alimento in self.alimentos:
            alimento.mostrarAlimento()

    def accederAlimento(self, id):
        for i, alimento in enumerate(self.alimentos):
            if alimento.id == id:
                return alimento
            else:
                print("Lo siento, este id no pertenece a ningún alimento")

    def hayAlimentosCategoria(self, tipoA):
        hayAlimento = False
        for i, alimento in enumerate(self.alimentos):
            if alimento.tipoA == tipoA:
                hayAlimento = True
        if hayAlimento == False:
            print("No hay alimentos de este tipo :c")
        return hayAlimento

    def mostrarAlimentosPorCategoria(self, tipoA):
        print("Alimentos para dieta", tipoA)
        for i, alimento in enumerate(self.alimentos):
            if alimento.tipoA == tipoA:
                alimento.mostrarAlimento()

    def liberarAlimento(self, id):
        for i, alimento in enumerate(self.alimentos):
            if alimento.id == id:
                self.alimentos.pop(i)

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def mostrarAnimales(self):
        print("Listado de animales: ")
        for animal in self.animales:
            animal.mostrarAnimal()

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