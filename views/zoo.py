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
        opcion = 1
        idH = 1
        idAn = 1
        idAl = 1
        print("***------ON-----***")
        print("Bienvenidos al zoológico")
        while opcion != 0:
            print("*------Menú-----*")
            print("1. Crear un habitat")
            print("2. Agregar un animal al zoológico")
            print("3. Agregar un animal al habitat")
            print("4. Mostrar habitats y animales disponibles")
            print("5. Agregar un alimento al zoológico")
            print("6. Alimentar a un animal de un habitat")
            opcion = int (input("Seleccione una opción: "))
            self.controlador.ejecutarOpcion(sistema, opcion, idH, idAn, idAl)

    def opcionUno(self, id):
        nombreH = input("Nombre del habitat: ")
        temperaturaH = input("Temperatura del habitat: ")
        tipoAH = input("Tipo de alimentación en el habitat: ")
        disponibilidad = int(input("Disponibilidad para animales: "))
        nuevoHabitat = habitatModel.Habitat(id, nombreH, temperaturaH, tipoAH, disponibilidad)
        print("El habitat ", nombreH, " ha sido creado exitosamente")

        return nuevoHabitat

    def opcionDos(self, id):
        nombreA = input("Ingrese el nombre del animal: ")
        edadA =  int(input("Ingrese la edad del animal: "))
        especieA = input("Ingrese la especie del animal: ")
        tipoA = input("Ingrese el tipo de alimentación: ")
        horasS = int(input("Ingrese las horas de sueño que necesita el animal: "))
        tiempoJuego = int(input("Ingrese el tiempo de juego adecuado para el animal: "))
        estadoSalud = int(input("Ingrese 1 si el animal está sano y 0 si no lo está: "))
        habitat = input("Ingrese el nombre del habitat al que pertenece el animal: ")

        nuevoAnimal = animalModel.Animal(id, nombreA, edadA, especieA, tipoA, horasS, tiempoJuego, estadoSalud, habitat)

        return nuevoAnimal

    def opcionTres(self, sistema):
        if len(sistema.animales) > 0 and len(sistema.habitats) > 0:
            print("Animales disponibles en el zoologico")
            sistema.listarAnimales()
            idAn = int(input("Ingrese el id del animal que desea agregar a un habitat:"))
            animalIngresar = sistema.accederAnimal(idAn)
            sistema.mostarHabitats()
            idH = int(input("Ingrese el id del habitat al que desea agregar el animal:"))
            habitatIngreso = sistema.accederAHabitat(idH)

            if (animalIngresar.tipoA == habitatIngreso.tipoAH) & (animalIngresar.habitat == habitatIngreso.nombreH):
                sistema.liberarAnimal(idAn)
                habitatIngreso.agregarAnimales(animalIngresar)
            else:
                print("Parece que el tipo de alimentación no es la misma, no puedes hacer esto :c")

        elif len(sistema.animales) > 0 >= len(sistema.habitats):
            print("Lo siento, aún no hay habitats disponibles")
        elif len(sistema.animales) <= 0 < len(sistema.habitats):
            print("Lo siento, no hay animales en el zoológico")
        else:
            print("Lo siento, no hay animales ni habitats disponibles en el zoológico aún")

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