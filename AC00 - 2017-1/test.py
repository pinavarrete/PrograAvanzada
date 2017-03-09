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


class GoldenPUC(Perro, Jugueton):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1.1
        else:
            self._expresion = self._expresion*0.9


class PUCTerrier(Perro, Egoista):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1.2
        else:
            self._expresion = self._expresion*1


class SiamePUC(Gato, Egoista):
    def __init__(self, expresion=1, **kwargs):
        super().__init__(**kwargs)
        self._expresion = expresion
        if self._sexo == "Macho":
            self._expresion = self._expresion*1
        else:
            self._expresion = self._expresion*1.5

    def cambio_expresion(self, animal=Gato):
        super().cambio_expresion(animal)


def accion(animal):
    animal.comer()
    animal.jugar()


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

    for a in animals:
        print(a)
        a.jugar()
        a.comer()
