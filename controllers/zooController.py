class ZooController:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutarOpcion(self, sistema, opcion, idH, idAn, idAl):
        if opcion == 1:
            nuevoHabitat = self.vista.opcionUno(idH)
            sistema.agregarHabitats(nuevoHabitat)
            idH += 1

        elif opcion == 2:
            nuevoAnimal = self.vista.opcionDos(idAn)
            sistema.agregarAnimales(nuevoAnimal)
            idAn += 1

        elif opcion == 3:
            self.vista.opcionTres(sistema)

        elif opcion == 4:
            sistema.mostarHabitats()

        elif opcion == 5:
            nuevoAlimento = self.vista.opcionCinco(idAl)

            sistema.agregarAlimentos(nuevoAlimento)
            idAl += 1

