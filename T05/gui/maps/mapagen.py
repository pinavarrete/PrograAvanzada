import csv
import random


def crear_etapa(numero):
    matriz = []
    paredes = {}
    for i in range(3):
        orientacion = random.randint(0, 1)
        if orientacion == 0:    #HORIZONTAL
            paredes[i] = (orientacion, random.randint(2,7))
        else:
            paredes[i] = (orientacion, random.randint(2, 19))
    for fila in range(10):
        line = 'B'
        for columna in range(21):
            if fila == 0 or fila == 9 or columna == 20:
                line = line + ',B'

            elif numero == 2 or numero == 3:
                if paredes[0][0] == 0:
                    if fila == paredes[0][1]:
                        if 1 < fila < 8 and 0 < columna < 19:
                            if numero == 2:
                                line = line + ',D'
                            else:
                                line = line + ',I'
                        else:
                            line = line + ',O'
                    else:
                        line = line + ',O'
                else:
                    if columna == paredes[0][1]:
                        if 1 < columna < 19 and 1 < fila < 8:
                            if numero == 2:
                                line = line + ',D'
                            else:
                                line = line + ',I'
                        else:
                            line = line + ',O'
                    else:
                        line = line + ',O'

            else:
                line = line + ',O'
        matriz.append(line)

    with open('Etapa' + str(numero) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for filas in range(len(matriz)):
            writer.writerow([matriz[filas]])

    print("Etapa {} creada exitosamente".format(numero))

if __name__ == '__main__':
    texto = "Ingrese el numero de etapa a generar \n"
    numero = input(texto)
    if numero.isnumeric():
        crear_etapa(int(numero))
    else:
        print('Ingrese un input válido por favor')
        numero = input(texto)
