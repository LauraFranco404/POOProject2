import streamlit as st


class Sistema:
    def __init__(self):
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        elif "habitats" not in st.session_state:
            self.habitats = []
            st.session_state["habitats"] = []
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        elif "animales" not in st.session_state:
            self.animales = []
            st.session_state["animales"] = []
        if "alimentos" in st.session_state:
            self.alimentos = st.session_state["alimentos"]
        elif "alimentos" not in st.session_state:
            self.alimentos = []
            st.session_state["alimentos"] = []


    def agregarHabitats(self, habitat):
        for habitatV in self.habitats:
            if habitatV.id == habitat.id:
                st.error("Parece que ya asignaste este id a otro habitat")
                return
            elif (habitatV.nombreH == habitat.nombreH) and (habitatV.tipoAH == habitat.tipoAH):
                st.error("Parece que hay otro habitat del mismo tipo y con la misma alimentación")
                return
            else:
                self.habitats.append(habitat)
                st.session_state["habitats"] = self.habitats
                print("El habitat ha sido agregado exitosamente")

    def accederAHabitat(self, id, habitats):
        for habitat in habitats:
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
        print("El animal ha sido agregado exitosamente")

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

#    def accederAnimal(self, id):
#        for i, animal in enumerate(self.animales):
#            if animal.id == id:
#                return animal
#            else:
#                print("Lo siento, este id no pertenece a ningún animal")