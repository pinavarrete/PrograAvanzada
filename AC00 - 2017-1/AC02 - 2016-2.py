from abc import ABCMeta, abstractmethod, abstractproperty


class Animal(metaclass=ABCMeta):
    def __init__(self):
        self._name = 'default_name'
        self._color = 'default_color'
        self._sexo = 'default_sexo'

    @abstractproperty
    def name(self):
        return self._name

    @abstractproperty
    def color(self):
        return self._color

    @abstractproperty
    def sexo(self):
        return self._sexo

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def jugar(self):
        pass


class Perro(Animal):
    def __init__(self, nombre='default_dog_name',
                 color='default_color', sexo='macho'):
        self._name = nombre
        self._color = color
        self._sexo = sexo
        self.factor = 1

    def __str__(self):
        return "Me llamo {}, soy {} y tengo pelo {}.".format(
                                                             self._name,
                                                             self._sexo,
                                                             self._color
        )

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def sexo(self):
        return self._sexo

    def comer(self):
        print('Mami :) Quiero comeeeeerr!!')

    def jugar(self):
        print('Tirame la pelota :)')

    def accion_propia(self):
        print('Guau!! Guau!!')


class Gato(Animal):
    def __init__(self, nombre='default_cat_name',
                 color='default_color', sexo='macho'):
        self._name = nombre
        self._color = color
        self._sexo = sexo
        self._factor = 1

    def __str__(self):
        return "Me llamo {}, soy {} y tengo pelo {}.".format(
                                                             self._name,
                                                             self._sexo,
                                                             self._color
        )

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def sexo(self):
        return self._sexo

    def comer(self):
        print('El pellet es horrible. Dame comida en lata.')

    def jugar(self):
        print('Humano, ahora, juguemos.')

    def accion_propia(self):
        print('Miauuu!! Miauuu!!')


class Personalidad(metaclass=ABCMeta):
    @abstractproperty
    def sleep_hours(self):
        pass

    @abstractproperty
    def play_individual_hours(self):
        pass

    @abstractproperty
    def play_grupal_hours(self):
        pass

    @abstractproperty
    def meals(self):
        pass

    @abstractproperty
    def love_hours(self):
        pass

    @abstractmethod
    def cambio_expresion(self):
        pass


class Jugueton(Personalidad):
    @property
    def sleep_hours(self):
        return 8

    @property
    def play_individual_hours(self):
        return 1

    @property
    def play_grupal_hours(self):
        return 7

    @property
    def meals(self):
        return 4

    @property
    def love_hours(self):
        return 4

    def cambio_expresion(self, animal):
        print("Quiero jugar.")
        animal.jugar()
        animal.accion_propia()


class Egoista(Personalidad):
    @property
    def sleep_hours(self):
        return 12

    @property
    def play_individual_hours(self):
        return 5

    @property
    def play_grupal_hours(self):
        return 1

    @property
    def meals(self):
        return 4

    @property
    def love_hours(self):
        return 2

    def cambio_expresion(self, animal):
        print("Quiero Comida")
        animal.comer()
        animal.accion_propia()


class GoldenPUC(Perro):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._personalidad = Jugueton()
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1.1
        else:
            self._expresion = self._expresion*0.9

    def jugar(self):
        print("Quiero Jugar")
        super().jugar()
        self.accion_propia()


class PUCTerrier(Perro):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._personalidad = Egoista()
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1.2
        else:
            self._expresion = self._expresion*1

    def comer(self):
        print("Quiero comida")
        super().comer()
        self.accion_propia()


class SiamePUC(Gato):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._personalidad = Egoista()
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1
        else:
            self._expresion = self._expresion*1.5

    def comer(self):
        print("Quiero comida")
        super().comer()
        self.accion_propia()


def sumar(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

if __name__ == '__main__':
    animals = list()
    animals.append(GoldenPUC(expresion=0.5, nombre="Mara",
                             color="Blanco", sexo="Hembra"))
    animals.append(GoldenPUC(expresion=0.9, nombre="Eddie",
                             color="Rubio", sexo="Macho"))
    animals.append(SiamePUC(expresion=0.9, nombre="Felix",
                            color="Naranjo", sexo="Hembra"))
    animals.append(PUCTerrier(expresion=0.8, nombre="Betty",
                              color="Café", sexo="Hembra"))

    horas_sueño = []
    horas_juego_indv = []
    horas_juego_grup = []
    cantidad_comida = []
    horas_regaloneao = []
    for animal in animals:
        horas_sueño.append(animal._personalidad.sleep_hours *
                           animal._expresion)
        horas_juego_indv.append(animal._personalidad.play_individual_hours *
                                animal._expresion)
        horas_juego_grup.append(animal._personalidad.play_grupal_hours *
                                animal._expresion)
        cantidad_comida.append(animal._personalidad.meals *
                               animal._expresion)
        horas_regaloneao.append(animal._personalidad.love_hours *
                                animal._expresion)
    print('Estadisticas')
    print('Horas de Sueño : {}'.format(min(horas_sueño)))
    print('Horas de Juego Individual : {}'.format(min(horas_juego_indv)))
    print('Horas de Juego Grupal : {}'.format(max(horas_juego_grup)))
    print('Horas de Comida : {}'.format(sumar(cantidad_comida)))
    print('Horas de Regaloneo : {}'.format(sumar(horas_regaloneao)))
    for a in animals:
        print(a)
        a.jugar()
        a.comer()
