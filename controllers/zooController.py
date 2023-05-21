import streamlit


class ZooController:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutarOpcion(self, sistema, opcion):
        if opcion == 1:
            try:
                nuevoHabitat = self.vista.opcionUno()
                if nuevoHabitat:
                    sistema.agregarHabitats(nuevoHabitat)
            except ValueError:
                self.vista.mostrarMensajeError("Se presentó un error creando el hábitat")

        elif opcion == 2:
            try:
                nuevoAnimal = self.vista.opcionDos()
                if nuevoAnimal:
                    sistema.agregarAnimales(nuevoAnimal)
            except ValueError:
                self.vista.mostrarMensajeError("Se presentó un error creando el animal")

        elif opcion == 3:
            self.vista.opcionTres(sistema)

        elif opcion == 4:
            self.vista.listarHabitats(sistema)
            self.vista.listarAnimalesLibres(sistema)
            self.vista.listarAnimalesPorHabitat(sistema)

        elif opcion == 5:
            try:
                nuevoAlimento = self.vista.opcionCinco()
                if nuevoAlimento:
                    sistema.agregarAlimentos(nuevoAlimento)
            except ValueError:
                self.vista.mostrarMensajeError("Se presentó un error creando el alimento")

        elif opcion == 6:
            self.vista.listarAlimentos(sistema)

        elif opcion == 7:
            self.vista.opcionSiete(sistema)

        elif opcion == 8:
            self.vista.opcionOcho(sistema)

        elif opcion == 9:
            self.vista.opcionNueve(sistema)

        elif opcion == 10:
            self.vista.opcionDiez()

    def aplicarFormatoTablaHabitats(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.id, habitat.nombreH, habitat.tipoAH, habitat.temperaturaH, habitat.disponibilidad])
        return datos

    def aplicarFormatoTablaAnimales(self, animales):
        datos = []
        for animal in animales:
            datos.append([animal.id, animal.nombre, animal.edad, animal.especie, animal.tipoA, animal.horasS, animal.tiempoJuego, animal.estadoSalud, animal.habitat, animal.estaJugando])
        return datos

    def aplicarFormatoTablaAnimalesHabitat(self, sistema, habitat):
        datos = []
        for animal in habitat.animales:
            datos.append([animal.id, animal.nombre, animal.edad, animal.especie, animal.tipoA, animal.horasS, animal.tiempoJuego, animal.estadoSalud, animal.habitat, animal.estaJugando])
        return datos

    def aplicarFormatoTablaAlimentos(self, alimentos):
        datos = []
        for alimento in alimentos:
            datos.append([alimento.id, alimento.nombre, alimento.tipoA])
        return datos