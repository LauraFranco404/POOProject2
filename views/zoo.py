import models.habitat as habitatModel
import models.animal as animalModel
import models.sistema as sistemaModel
import models.alimento as alimentoModel
import controllers.zooController as zooController
import streamlit as st
import pandas as pd


class Zoo:
    def __init__(self):
        self.sistema = sistemaModel.Sistema()
        self.controlador = zooController.ZooController(self.sistema, self)

    def mostrarMenu(self, sistema):
        st.title("Bienvenido al Zooológico RF")


        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Crear un habitat")
            botonCrearHabitat = col1.button("Acceder a esta opción", 1)
            col2.header("Agregar un animal al zoológico")
            botonAgregarAnimal = col2.button("Acceder a esta opción", 2)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Agregar un animal a un habitat")
            botonAgregarAnimalH = col1.button("Acceder a esta opción", 3)
            col2.header("Mostrar habitats y animales disponibles")
            botonMostrarH = col2.button("Acceder a esta opción", 4)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Agregar un animal al zoológico")
            botonAgregarAlimento = col1.button("Acceder a esta opción", 5)
            col2.header("Alimentar a un animal de un habitat")
            botonAlimentar = col2.button("Acceder a esta opción", 6)

        if botonCrearHabitat:
            st.session_state["opcion"] = 1
        elif botonAgregarAnimal:
            st.session_state["opcion"] = 2
        elif botonAgregarAnimalH:
            st.session_state["opcion"] = 3
        elif botonMostrarH:
            st.session_state["opcion"] = 4
        elif botonAgregarAlimento:
            st.session_state["opcion"] = 5
        elif botonAlimentar:
            st.session_state["opcion"] = 6

        if "opcion" in st.session_state:
            self.controlador.ejecutarOpcion(sistema, st.session_state["opcion"])

    def opcionUno(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            id = st.number_input("ID del habitat:", min_value=1, step=1)
            nombreH = st.selectbox("Nombre del habitat:", ("Acuático", "Desértico", "Polar", "Selvático"))
            temperaturaH = st.number_input("Temperatura:", step=1)
            tipoAH = st.selectbox("Tipo de alimentación en el habitat", ("Carnívora", "Hervíbora", "Omnívora"))
            disponibilidad = st.number_input("Disponibilidad para animales", min_value=0, max_value=100)
            botonAccion = st.button("Crear nuevo habitat")

        if botonAccion:
            nuevoHabitat = habitatModel.Habitat(id, nombreH, temperaturaH, tipoAH, disponibilidad)
            st.success("El habitat ha sido creado exitosamente")
            return nuevoHabitat

    def opcionDos(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para agregar un animal al zoológico")
            id = st.number_input("ID del animal:", min_value=1, step=1)
            nombreA = st.text_input("Nombre del animal:")
            edadA = st.number_input("Edad del animal:", min_value=0, max_value=100, step=1)
            especieA = st.text_input("Especie del animal:")
            tipoA = st.selectbox("Tipo de alimentación del animal", ("Carnívora", "Hervíbora", "Omnívora"))
            horasS = st.number_input("Horas de sueño del animal:", min_value=8, max_value=20, step=1)
            tiempoJuego = st.number_input("Tiempo de juego del animal:", min_value=1, max_value=4, step=1)
            estadoSalud = st.checkbox("¿Animal sano?")
            if estadoSalud:
                st.write("El animal está sano c:")
            habitatA = st.selectbox("Nombre del habitat al que pertenece el animal:", ("Acuático", "Desértico", "Polar", "Selvático"))
            botonAccion = st.button("Agregar nuevo animal")
            if botonAccion:
                nuevoAnimal = animalModel.Animal(id, nombreA, edadA, especieA, tipoA, horasS, tiempoJuego, estadoSalud,habitatA)
                st.success("El animal ha sido ingresado exitosamente")
                return nuevoAnimal

    def listarHabitats(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Listado de habitats disponibles")
            if len(sistema.habitats) == 0:
                st.error("No hay habitats para mostrar")
            else:
                datos = pd.DataFrame(
                    self.controlador.aplicarFormatoTablaHabitats(sistema.habitats),
                    columns=["ID del habitat", "Nombre del habitat", "Tipo de alimentación en el habitat", "Temperatura del habitat", "disponibilidad"]
                )
                st.table(datos)

    def opcionTres(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Formulario para ingresar un animal a un habitat")

            if len(sistema.habitats) == len(sistema.animales) == 0:
                print("Lo siento, no hay animales ni habitats disponibles en el zoológico aún")

            elif len(sistema.animales) == 0:
                st.error("No hay animales libres en el zoológico")

            elif len(sistema.habitats) == 0:
                st.error("Lo siento, parece que aún no hay hábitats disponibles en el zoológico")

            else:
                opcionesA = []
                opcionesH = []
                for animal in sistema.animales:
                    opcionesA.append([animal.id, animal.nombre, animal.habitat, animal.tipoA])

                idAn = st.selectbox("Animal que desea agregar a un habitat:", opcionesA)
                idAnimal = animal.id
                animalSeleccionado = self.accederAnimal(idAnimal, sistema.animales)

                for habitat in sistema.habitats:
                    opcionesH.append([habitat.id, habitat.nombreH, habitat.tipoAH])

                idH = st.selectbox("Habitat al que desea ingresar el animal", opcionesH)
                idHabitat = habitat.id
                habitatIngreso = self.obtenerInformacionHabitat(idHabitat, sistema.habitats)
                botonAccion = st.button("Agregar animal a habitat")
                if botonAccion:
                    if (animalSeleccionado.tipoA == habitatIngreso.tipoAH) & (animalSeleccionado.habitat == habitatIngreso.nombreH):
                        sistema.liberarAnimal(idAnimal)
                        habitatIngreso.agregarAnimales(animalSeleccionado)
                        st.success("El animal fue ingresado al habitat correctamente")
                    else:
                        st.error("Parece que el tipo de alimentación no es la misma, no puedes hacer esto :c")

    def obtenerInformacionHabitat(self, id, habitats):
        for habitat in habitats:
            if habitat.id == id:
                return habitat
            else:
                print("error")

    def accederAnimal(self, id, animales):
        for animal in animales:
            if animal.id == id:
                return animal

    def opcionCinco(self, id):
        nombreAl = input("Ingrese el alimento del animal")
        tipoAl = input("Ingrese la categoría a la que pertenece el alimento")
        nuevoAlimento = alimentoModel.Alimento(id, nombreAl, tipoAl)
        print("El alimento", nuevoAlimento.nombre, "ha sido creado exitosamente")
        return nuevoAlimento

    def opcionSeis(self, sistema):
        sistema.mostarHabitats()
        idH = int(input("Seleccione el id del habitat en el que se encuentra el animal que desea alimentar:"))
        habitatIngreso = sistema.accederAHabitat(idH)
        if len(habitatIngreso.animales) > 0:
            idA = int(input("Seleccione el id del animal que desea alimentar:"))
            animalAlimentar = sistema.accederAnimal(idA)
            hayAlimento = sistema.hayAlimentosCategoria(habitatIngreso.tipoAH)
            if hayAlimento:
                sistema.mostrarAlimentosPorCategoria(habitatIngreso.tipoAH)
                idAl = int(input("Seleccione un id de alimento para alimentar al animal"))
                alimento = sistema.accederAlimento(idAl)
                if alimento.tipoA == habitatIngreso.tipoAH:
                    sistema.liberarAlimento(idAl)
                    print("Ñomi, has alimentado a", animalAlimentar.nombre, "con", alimento.nombre)
                else:
                    print("Lo siento, esto no corresponde a su dieta")
            else:
                print("Lo siento, aún no tienes alimentos de esta categoría :c")

    def mostraMensajeError(self, mensaje):
        st.error(mensaje)
