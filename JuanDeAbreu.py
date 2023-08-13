import random
fechazeus = "20/2/2022"


def animalitosuwu(nombredelanimal, numregi):

    def registrado():

        if nombredelanimal == "Zeus" and numregi == 10:

            print("La ultima revisión de" +
                  nombredelanimal+" fue el día "+fechazeus)

            revi = input("Desea hacerle otra revisión(si,no) ")

            if revi == "si":

                datcuenta = input("ingrese los datos de la cuenta: ")
                print("Será atendido en un segundo")

            else:
                print("Gracias por confiarnos su mascota,vuelva pronto")

            return True

    if num == 0:
        numregi = random.randint(0, 1000)
        nombredelanimal = nom
        print("Su número de registro será el siguiente:", numregi)
    else:
        return registrado()


nom = input("Cual es el nombre de su mascota?(Primera letra mayuscula)   ")
num = int(input("Ingrese el número de registro(si no tiene uno ponga el 0):  "))

animalitosuwu(nom, num)
