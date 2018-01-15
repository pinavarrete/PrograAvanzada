import time
import datetime


def cambiar_numeros(numero):
    cambios = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "0", "0": "5",
               "6": "4", "7": "3", "8": "2", "9": "1"}
    a = ""
    for char in numero:
        a += cambios[char]
    return a[::-1]


def numeros_primos():
    i = 2
    while True:
        if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (
            i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7):
            yield i
        i += 1


def numeros_malvados():
    i = 1
    while True:
        if bin(i).count("1") % 2 == 0:
            yield i
        i += 1


with open("chatayudantes.iic2233", "rb") as file:
    f = file.read()

a = 0
suma = 0
archivo = bytearray()
for i in f:
    if a == 4:
        suma = str(suma)
        if len(suma) == 1:
            suma = "00"+suma
        if len(suma) == 2:
            suma = "0"+suma
        archivo += bytes([int(cambiar_numeros(suma))])
        a = 1
        suma = i
    else:
        suma += i
        a += 1

audio = bytearray()
imagen = bytearray()

terminado = False
primos = numeros_primos()
malvados = numeros_malvados()
primo = next(primos)
malvado = next(malvados)

n = 0
pos = 0
terminado = False

while not terminado:  # ><
    if n % 2 == 0:
        if len(audio) + len(archivo[pos:pos + primo]) > 9783:
            value = 9783 - len(audio) + pos
            audio += bytearray(archivo[pos:value])
            imagen += bytearray(archivo[value:])
            terminado = True
        else:
            audio += bytearray(archivo[pos:pos + primo])
            pos += primo
            primo = next(primos)

    if n % 2 == 1:
        imagen += bytearray(archivo[pos:pos + malvado])
        pos += malvado
        malvado = next(malvados)

    n += 1

auxiliar = bytearray()
contador = 0

print(imagen[:5])

with open("audio.wav", "wb") as file:
    for i in audio:
        auxiliar += bytes([i])
        contador += 1
        if contador == 512:
            file.write(auxiliar)
            auxiliar = bytearray()
            contador = 0
    file.write(auxiliar)

auxiliar = bytearray()
contador = 0

with open("imagen.gif", "wb") as f:
    for i in imagen:
        auxiliar += bytes([i])
        contador += 1
        if contador == 1024:
            f.write(auxiliar)
            auxiliar = bytearray()
            contador = 0
    f.write(auxiliar)
