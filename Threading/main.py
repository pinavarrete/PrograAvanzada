from threading import Thread
from functools import reduce
import random


class Torre:

    def __init__(self, equipo, health_ponts=100):
        self._hp = health_ponts
        self._viva = True
        self.equipo = equipo

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if self._hp - value > 0:
            self._hp -= value
            print('[TORRE] Ha recibido {} de daño'.format(value))
        else:
            self._hp = 0
            self._viva = False
            print('[TORRE] Se ha caído la Torre'.format(value))

    @property
    def con_vida(self):
        return self._viva


class Soldado(Thread):

    def __init__(self, equipo, health_ponts=100):
        self._hp = health_ponts
        self._vivo = True
        self.equipo = equipo
        self.ataques = list()
        self.enemigos = {'Tower': None, 'Soldiers': list()}

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if self._hp - value > 0:
            self._hp -= value
            print('[SOLDADO] Ha recibido {} de daño'.format(value))
        else:
            self._hp = 0
            self._viva = False
            print('[SOLDADO] Ha muerto un soldado'.format(value))

    def atacar_soldado(self, total_soldados):
        pos_soldado = random.randint(0, len(total_soldados))
        return (50, pos_soldado)

    def atacar_torre(self):
        return 10


class FrancoTirador(Thread):

    def __init__(self, equipo):
        self.equipo = equipo
        self.ataques = list()
        self.enemigos = {'Soldiers': list()}

    def atacar_soldado(self, total_soldados):
        pos_soldado = random.randint(0, len(total_soldados))
        return (100, pos_soldado)


if __name__ == '__main__':
    for i in range(10):
        proms = list()
        for _ in range(1000):
            values = [random.randint(5, 10) for _ in range(5)]
            proms.append(reduce(lambda x, y: x+y, values)/len(values))
        print(6*reduce(lambda x, y: x+y, proms)/len(proms))
