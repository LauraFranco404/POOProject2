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

        elif opcion == 5:
            nuevoAlimento = self.vista.opcionCinco()

            sistema.agregarAlimentos(nuevoAlimento)

    def aplicarFormatoTablaHabitats(self, habitats):
        datos = []
        for habitat in habitats:
            datos.append([habitat.id, habitat.nombreH, habitat.tipoAH, habitat.temperaturaH, habitat.disponibilidad])
            return datos
