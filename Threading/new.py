from threading import Thread, Lock
import random
import time


def spawn_personas(lista_personas, partida, final):
    while True:
        time.sleep(random.expovariate(5))
        persona = Persona(partida, final)
        lista_personas.append(persona)
        persona.setDaemon(True)
        persona.start()


class Barrendero(Thread):

    def __init__(self, vivas, muertas):
        super().__init__()
        self.muertas = muertas
        self.vivas = vivas

    def run(self):
        while True:
            time.sleep(1)
            for persona in self.vivas:
                if persona.morir:
                    self.vivas.remove(persona)
                    self.muertas.append(persona)


class Laberinto(Thread):

    def __init__(self):
        super().__init__()
        self.partida = 0
        self.termino = 0
        self.lista_nodos = list()
        self.muertos = list()
        self.lista_salir = list()
        self.lista_personas = list()
        self.cargar_laberinto()
        self.barrendero = Barrendero(self.lista_personas, self.muertos)

    def cargar_laberinto(self):
        lista_piezas = open('laberinto.txt', 'r')
        reader = [x.split(',') for x in lista_piezas]
        reader = [[int(x.strip('\n')) for x in nueva_linea] for nueva_linea in reader]
        self.partida = reader[0][0]
        self.termino = reader[1][0]
        self.lista_nodos = [Nodo(i+1) for i in range(self.termino)]

        for x in reader[2::]:
            self.lista_nodos[x[0]-1].direcciones.append(self.lista_nodos[x[1]-1])

    def start(self):
        inicio = self.lista_nodos[0]
        final = self.lista_nodos[self.termino-1]
        spawner = Thread(target=spawn_personas, args=(self.lista_personas, inicio, final), daemon=True)
        spawner.start()
        while len(self.lista_salir) < 3:
            for persona in self.lista_personas:
                if persona.salir:
                    self.lista_salir.append(persona)
                    self.lista_personas.remove(persona)
        print('Han salido {} personas'.format(len(self.lista_salir)))


class Persona(Thread):

    num_persona = 0

    def __init__(self, partida, final, hp=random.randint(80, 120), resistencia=random.randint(1, 3)):
        self.id = Persona.num_persona + 1
        Persona.num_persona += 1
        self.final = final
        self.pieza_actual = partida
        self._hp = hp
        self.resistencia = resistencia
        self.salir = False
        self.morir = False
        super().__init__()

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if self._hp - (6 - self.resistencia) > 0:
            self._hp = self._hp - (6 - self.resistencia)
        else:
            self._hp = 0

    def run(self):
        print('persona {}, entra'.format(self.id))
        while True:
            self.mover(self.pieza_actual.direcciones)
            print('Persona {} en pieza {}'.format(self.id, self.pieza_actual))
            if self.salir:
                break
        print('Persona {}, salí del Laberinto Wiiiiiiiiiiiiiiiiii'.format(self.id))

    def mover(self, lista_nodo):
        if len(lista_nodo) > 0:
            nodo_destino = random.choice(lista_nodo)
            with nodo_destino.ocupado:
                self.pieza_actual = nodo_destino
                time.sleep(random.randint(1, 3))
                if self.pieza_actual == self.final:
                    self.salir = True
        else:
            Persona.morir = True


class Nodo:

    def __init__(self, id_nodo):
        self.id = id_nodo
        self.direcciones = []
        self.ocupado = Lock()

    def __repr__(self):
        return 'Class Nodo Id {}'.format(self.id)


lab = Laberinto()
lab.start()
# n = lab.lista_nodos[1].direcciones
# print(n)
