import time
import datetime


def cambiar_numeros(numero):
    cambios = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "0", "0": "5", "6": "4", "7": "3", "8": "2", "9": "1"}
    a = ""
    for char in numero:
        a += cambios[char]
    return a[::-1]

def numeros_primos():
    i = 2
    while True:
        if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7):
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

print(len(f))

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
        suma = i
        a = 1
    else:
        suma += i
        a += 1

print('aqui')
print(len(archivo))

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

while not terminado: # ><


    if n % 2 == 0:
        if len(audio) + len(archivo[pos:pos + primo]) > 9783:
            value = 9783 - len(audio)
            audio += bytearray(archivo[pos:pos + value])
            imagen += bytearray(archivo[pos + value:])
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

print(imagen[:5])
for _ in imagen[:5]:
    print(_)

print(audio[:5])
for _ in audio[:5]:
    print(_)

auxiliar = bytearray()
contador = 0
contador2 = 0
t0 = time.time()
with open("audio.wav", "wb") as file:
    print("{0:8s}{1: ^9s}    {2: <8s} {3: >7s}".format("Total", "Procesado", "Sin Procesar", "DeltaTime"))
    for i in audio:
        auxiliar += bytes([i])
        contador += 1
        contador2 += 1
        if contador == 512:
            print("{0:8d}{1: ^9d}    {2: <8d}{3: >7.4f}".format(len(audio), contador2,
                                                                    len(audio) - contador2 , time.time()-t0))

            file.write(auxiliar)
            auxiliar = bytearray()
            contador = 0
    print("{0:8d}{1: ^9d}    {2: <8d}{3: >7.4f}".format(len(audio), contador2,
                                                        len(audio) - contador2, time.time() - t0))

    file.write(auxiliar)

auxiliar = bytearray()
contador = 0
t0 = time.time()
contador2 = 0
with open("imagen.gif", "wb") as f:
    print("{0:8s}{1: ^9s}    {2: <8s} {3: >7s}".format("Total", "Procesado", "Sin Procesar", "DeltaTime"))
    for i in imagen:
        auxiliar += bytes([i])
        contador += 1
        contador2 += 1
        if contador == 1024:
            print("{0:8d}{1: ^9d}    {2: <8d}{3: >7.4f}".format(len(imagen), contador2,
                                                                    len(imagen) - contador2 , time.time()-t0))
            f.write(auxiliar)
            auxiliar = bytearray()
            contador = 0
    print("{0:8d}{1: ^9d}    {2: <8d}{3: >7.4f}".format(len(imagen), contador2,
                                                        len(imagen) - contador2, time.time() - t0))
    f.write(auxiliar)
