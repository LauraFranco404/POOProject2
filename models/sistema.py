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
        flag = 1
        for habitatV in self.habitats:
            if habitatV.id == habitat.id:
                st.error("Parece que ya asignaste este id a otro habitat")
                flag = 0
            elif (habitatV.nombreH == habitat.nombreH) and (habitatV.tipoAH == habitat.tipoAH):
                st.error("Parece que hay otro habitat del mismo tipo y con la misma alimentación")
                flag = 0
        if flag == 1:
            self.habitats.append(habitat)
            st.session_state["habitats"] = self.habitats
            st.success("El habitat ha sido agregado exitosamente")
        else:
            st.error("Lo siento, el habitat no se pudo ingresar")

    def agregarAlimentos(self, alimento):
        flag = 1
        for alimentoV in self.alimentos:
            if alimentoV.id == alimento.id:
                st.error("Parece que ya asignaste este id a otro alimento")
                flag = 0
        if flag == 1:
            self.alimentos.append(alimento)
            st.success("El alimento ha sido agregado exitosamente")
        else:
            st.error("Lo siento, el alimento no se pudo ingresar")

    def liberarAlimento(self, id):
        for i, alimento in enumerate(self.alimentos):
            if alimento.id == id:
                self.alimentos.pop(i)

    def agregarAnimales(self, animal):
        flag = 1
        for animalV in self.animales:
            if animalV.id == animal.id:
                st.error("Parece que ya asignaste este id a otro animal")
                flag = 0
        if flag == 1:
            self.animales.append(animal)
            st.success("El animal ha sido agregado exitosamente")
        else:
            st.error("Lo siento, el animal no se pudo ingresar")

    def liberarAnimal(self, id):
        for i, animal in enumerate(self.animales):
            if animal.id == id:
                self.animales.pop(i)
