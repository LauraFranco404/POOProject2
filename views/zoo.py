import models.habitat as habitatModel
import models.animal as animalModel
import models.sistema as sistemaModel
import models.alimento as alimentoModel
import controllers.zooController as zooController
import streamlit as st
import pandas as pd
import requests


class Zoo:
    def __init__(self):
        self.sistema = sistemaModel.Sistema()
        self.controlador = zooController.ZooController(self.sistema, self)

    # Esta opción modela los encabezados en streamlit y se encarga de darles formato y tomar la opción que salga de
    # la selección de cada botón
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
            col1.header("Agregar un alimento al zoológico")
            botonAgregarAlimento = col1.button("Acceder a esta opción", 5)
            col2.header("Mostrar alimentos en el zoológico")
            botonMostrarAlimento = col2.button("Acceder a esta opción", 6)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Alimentar a un animal")
            botonAlimentar = col1.button("Acceder a esta opción", 7)
            col2.header("Llevar a dormir a un animal")
            botonDormir = col2.button("Acceder a esta opción", 8)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Jugar con un animal")
            botonJugar = col1.button("Jugar con un animal", 9)
            col2.header("Mira nuestras mascotas :)")
            botonConsulta = col2.button("Acceder a esta opción", 10)

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
        elif botonMostrarAlimento:
            st.session_state["opcion"] = 6
        elif botonAlimentar:
            st.session_state["opcion"] = 7
        elif botonDormir:
            st.session_state["opcion"] = 8
        elif botonJugar:
            st.session_state["opcion"] = 9
        elif botonConsulta:
            st.session_state["opcion"] = 10

        if "opcion" in st.session_state:
            self.controlador.ejecutarOpcion(sistema, st.session_state["opcion"])

    # Aquí se crea el formato que se mostrará en pantalla para pedir los datos al usuario
    # y guardar la información que se le dará a la misma función
    # para que cree un habitat y lo retorne para agregarlo finalmente en el sistema
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
            print("El habitat ha sido creado exitosamente")
            return nuevoHabitat

    # Aquí se crea el formato que se mostrará en pantalla para pedir los datos al usuario
    # y guardar la información que se le dará a la misma función
    # para que cree un animal y lo retorne para agregarlo finalmente en el sistema
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
            estadoSalud = st.selectbox("Estado de salud del animal: ", ("Sano", "No sano"))
            habitatA = st.selectbox("Nombre del habitat al que pertenece el animal:", ("Acuático", "Desértico", "Polar", "Selvático"))
            botonAccion = st.button("Agregar nuevo animal")
            if botonAccion:
                nuevoAnimal = animalModel.Animal(id, nombreA, edadA, especieA, tipoA, horasS, tiempoJuego, estadoSalud,habitatA)
                st.success("El animal ha sido ingresado exitosamente")
                return nuevoAnimal

    # Esta función se encarga de mostrar en un formato de tabla (con ayuda de la función en el controlador)
    # la información de los habitats disponibles en el zoológico en ese momento
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

    # Esta función se encarga de mostrar en un formato de tabla (con ayuda de la función en el controlador)
    # la información de los animales disponibles en el refugio del zoológico en ese momento
    def listarAnimalesLibres(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Listado de animales en refugio")
            if len(sistema.animales) == 0:
                st.error("No hay animales para mostrar")
            else:
                datos = pd.DataFrame(
                    self.controlador.aplicarFormatoTablaAnimales(sistema.animales),
                    columns=["ID del animal", "Nombre del animal", "Edad del animal", "Especie del animal", "Tipo de alimentación del animal", "Horas de sueño del animal", "Tiempo de juego del animal", "Estado de salud del animal", "Habitat del animal", "Ha jugado en el día"]
                )
                st.table(datos)

    # Esta función se encarga de mostrar en un formato de tabla (con ayuda de la función en el controlador)
    # la información de los animales disponibles en cada uno de los habitats disponibles en el sistema
    def listarAnimalesPorHabitat(self, sistema):
        st.divider()
        if len(sistema.habitats) == 0:
            st.error("No hay habitats para mostrar")
        else:
            st.subheader("Listado de animales disponibles en el habitat"),
            for habitat in sistema.habitats:
                st.subheader(habitat.nombreH)
                if len(habitat.animales) == 0:
                    st.error("No hay animales en este habitat aún")
                else:
                    with st.container():
                            datos = pd.DataFrame(
                                self.controlador.aplicarFormatoTablaAnimalesHabitat(habitat),
                                columns=["ID del animal", "Nombre del animal", "Edad del animal", "Especie del animal", "Tipo de alimentación del animal", "Horas de sueño del animal", "Tiempo de juego del animal", "Estado de salud del animal", "Habitat del animal", "Ha jugado en el día"]
                            )
                            st.table(datos)

    # Esta función se encarga de mirar si en el sistema hay habitats o animales en refugio, en casode haber ambos
    # accederá al animal que se indique y al habitat al que se intente ingresar y realizará la comparación de
    # dos variables: el tipo de alimentación y el nombre del habitat, para intentar ingresar al animal
    # si hay disponibilidad
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
                idAnimal = idAn[0]
                animalSeleccionado = self.accederAnimal(idAnimal, sistema.animales)

                for habitat in sistema.habitats:
                    opcionesH.append([habitat.id, habitat.nombreH, habitat.tipoAH])

                idH = st.selectbox("Habitat al que desea ingresar el animal", opcionesH)
                idHabitat = idH[0]
                habitatIngreso = self.obtenerInformacionHabitat(idHabitat, sistema.habitats)
                botonAccion = st.button("Agregar animal a habitat")

                if botonAccion:

                    if (animalSeleccionado.tipoA == habitatIngreso.tipoAH) and (animalSeleccionado.habitat == habitatIngreso.nombreH):
                        if habitatIngreso.disponibilidad > 0:
                            sistema.liberarAnimal(idAnimal)
                            habitatIngreso.agregarAnimales(animalSeleccionado)
                            habitatIngreso.disponibilidad -= 1
                            st.success("El animal fue ingresado al habitat correctamente")
                        else:
                            st.error("Lo siento, no caben más animalitos en el habitat")
                    else:
                        st.error("Parece que la información no concuerda, no puedes hacer esto :c")

    # Esta función se encargará de buscar en una lista de habitats un objeto cuyo identificador sea el id
    # que se pasa por parámetro y luego lo retorna
    def obtenerInformacionHabitat(self, id, habitats):
        for habitat in habitats:
            if habitat.id == id:
                return habitat

    # Esta función se encargará de buscar en una lista de animales un objeto cuyo identificador sea el id
    # que se pasa por parámetro y luego lo retorna
    def accederAnimal(self, id, animales):
        for animal in animales:
            if animal.id == id:
                return animal

    # Esta función se encargará de buscar en una lista de alimentos un objeto cuyo identificador sea el id
    # que se pasa por parámetro y luego lo retorna
    def accederAlimento(self, id, alimentos):
        for alimento in alimentos:
            if alimento.id  == id:
                return alimento

    # Aquí se crea el formato que se mostrará en pantalla para pedir los datos al usuario
    # y guardar la información que se le dará a la misma función
    # para que cree un alimento y lo retorne para agregarlo finalmente en el sistema
    def opcionCinco(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo aliemnto")
            id = st.number_input("ID del alimento:", min_value=1, step=1)
            nombreAl = st.text_input("Nombre del Alimento:")
            tipoAl = st.selectbox("Categoría del alimento", ("Carnívora", "Hervíbora", "Omnívora"))
            botonAccion = st.button("Crear nuevo alimento")

        if botonAccion:
            nuevoAlimento = alimentoModel.Alimento(id, nombreAl, tipoAl)
            print("El alimento ha sido creado exitosamente")
            return nuevoAlimento


    # Esta función se encarga de mostrar en un formato de tabla (con ayuda de la función en el controlador)
    # la información de los alimentos disponibles en el sistema
    def listarAlimentos(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Listado de alimentos disponibles")
            if len(sistema.alimentos) == 0:
                st.error("No hay alimentos para mostrar")
            else:
                datos = pd.DataFrame(
                    self.controlador.aplicarFormatoTablaAlimentos(sistema.alimentos),
                    columns=["ID del alimento", "Nombre del alimento", "Categoría del alimento"]
                )
                st.table(datos)

    # Esta función se encarga de mostrar en una barra de selección todos los animales y en otra todos los alimentos
    # disponibles en el sistema. Después de seleccionarlos, comparará si la categoría del alimento es la misma
    # y entonces alimentará al animal
    def opcionSiete(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Formulario para alimentar a un animal")
            if(len(sistema.habitats)) == 0 and (len(sistema.alimentos) == 0):
                st.error("Lo siento, parece que aún no hay hábitats ni alimentos disponibles en el zoológico")
            elif len(sistema.alimentos) == 0:
                st.error("Lo siento, parece que aún no hay alimentos disponibles")
            else:
                opcionesA = []
                opcionesAl = []
                for habitat in sistema.habitats:
                    idHabitat = habitat.id
                    habitatIngreso = self.obtenerInformacionHabitat(idHabitat, sistema.habitats)
                    if len(habitatIngreso.animales) > 0:
                        for animal in habitatIngreso.animales:
                            opcionesA.append([animal.id, animal.nombre, animal.habitat, animal.tipoA, habitatIngreso.id])
                idA = st.selectbox("Animal al que desea alimentar", opcionesA)
                nHabitatIngreso = self.obtenerInformacionHabitat(idA[4], sistema.habitats)
                animalAlimentar = self.accederAnimal(idA[0], nHabitatIngreso.animales)
                for alimento in sistema.alimentos:
                    opcionesAl.append([alimento.id, alimento.nombre, alimento.tipoA])
                idAl = st.selectbox("Alimento que desea ofrecer al animal", opcionesAl)
                idALimento = alimento.id
                alimentoDar = self.accederAlimento(idALimento, sistema.alimentos)
                botonAccion = st.button("Alimentar animal")
                if botonAccion:
                    if animalAlimentar.tipoA == alimentoDar.tipoA:
                        sistema.liberarAlimento(idALimento)
                        st.success("Ha alimentado al animal")
                    else:
                        st.error("Lo siento, al parecer no puedes hacer eso")

    # Esta función se encarga de mostrar en una barra de selección todos los animales disponibles en el sistema.
    # Después de seleccionar un animal, presentará la opción de seleccionar las horas que se quiere que el animal duerma
    # se compararán entonces estas horas y solo si son suficientes y si el animal no ha dormido, se cambiará su atributo
    # de haDormido por "Ha dormido"
    def opcionOcho(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Formulario para llevar a dormir a un animal")
            if len(sistema.habitats) == 0:
                st.error("Lo siento, parece que aún no hay hábitats ni alimentos disponibles en el zoológico")
            else:
                opcionesA = []
                for habitat in sistema.habitats:
                    idHabitat = habitat.id
                    habitatIngreso = self.obtenerInformacionHabitat(idHabitat, sistema.habitats)
                    if len(habitatIngreso.animales) > 0:
                        for animal in habitatIngreso.animales:
                            opcionesA.append([animal.id, animal.nombre, animal.habitat, animal.horasS, animal.haDormido, habitatIngreso.id])
                idA = st.selectbox("Animal al que desea llevar a dormir", opcionesA)
                nHabitatIngreso = self.obtenerInformacionHabitat(idA[5], sistema.habitats)
                animalDormir = self.accederAnimal(idA[0], nHabitatIngreso.animales)
                horasDormir = st.number_input("Horas que desea llevar al animal a dormir:", min_value=0, max_value=20, step=1)
                botonAccion = st.button("LLevar a dormir al animal")
                if botonAccion:
                    if animalDormir.haDormido == "Ha dormido":
                        st.error("Lo siento, este animal ya ha dormido")
                    elif animalDormir.horasS < horasDormir:
                        st.error("Lo siento, el animal no puede dormir tanto")
                    elif animalDormir.horasS > horasDormir:
                        st.error("Lo siento, el animal no puede dormir tan poco")
                    else:
                        animalDormir.haDormido = "Ha dormido"
                        st.success("El animal se ha ido a dormir:")
                        st.success("_Zzzz_")

    # Esta función se encarga de mostrar en una barra de selección todos los animales disponibles en el sistema.
    # Después de seleccionar un animal, presentará la opción de llevarlo a jugar
    # se verá entonces si el animal ha jugado en el día y solo si el animal no ha jugado, se cambiará su atributo
    # de estaJugando por "Ha jugado"
    def opcionNueve(self, sistema):
        st.divider()
        with st.container():
            st.subheader("Formulario para llevar a jugar a un animal")
            if len(sistema.habitats) == 0:
                st.error("Lo siento, parece que aún no hay hábitats ni alimentos disponibles en el zoológico")
            else:
                opcionesA = []
                for habitat in sistema.habitats:
                    idHabitat = habitat.id
                    habitatIngreso = self.obtenerInformacionHabitat(idHabitat, sistema.habitats)
                    if len(habitatIngreso.animales) > 0:
                        for animal in habitatIngreso.animales:
                            opcionesA.append([animal.id, animal.nombre, animal.habitat, animal.horasS, animal.estaJugando, habitatIngreso.id])
                idA = st.selectbox("Animal al que desea sacar a jugar", opcionesA)
                nHabitatIngreso = self.obtenerInformacionHabitat(idA[5], sistema.habitats)
                animalJugar = self.accederAnimal(idA[0], nHabitatIngreso.animales)
                botonAccion = st.button("Llevar a jugar")
                if botonAccion:
                    if animalJugar.estaJugando == "Ha jugado":
                        st.error("Lo siento, este animal ya ha jugado")
                    else:
                        animalJugar.estaJugando = "Ha jugado"
                        st.success("¡El animal se está divirtiendo mucho!")
                        st.success("_He, He_")

    # Esta función se encarga de traer información de una API que muestra imágenes aleatorias de perritos
    def opcionDiez(self):
        llamado = requests.get("https://dog.ceo/api/breeds/image/random")
        datos = llamado.json()
        dato = datos['message']
        st.success("Jeje, aquí tiene una imagen que le alegrará el día :)")
        st.markdown(f'''<a href={dato}><button style="background-color:Green;">¡Perritos!</button></a>''', unsafe_allow_html=True)
        print(dato)


