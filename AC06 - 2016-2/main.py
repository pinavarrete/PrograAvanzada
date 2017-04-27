__author__ = "Juan Cortes, Cristian Cortes, Manuel Silva"


def is_pokemon(f):

    def _is_pokemon(*args):
        if isinstance(args[1], Pokemon):
            args[0].pokemon.append(args[1])
        else:
            return None
    return _is_pokemon


def my_name(f):

    def _myname(*args):
        clase = args[0]
        return clase.nombre
    return _myname


def protect_method(*args):

    def __protect_methods(*args):
        clase = args[0]
        for arg in args:
            if type(arg) != type(clase):
                print(arg)
                if not getattr(clase, arg):
                    print(arg + ' no es un método de clase')
                else:
                    setattr(clase, '_'+arg, arg)
                    if clase.owner == 'Prof. Oak':
                        clase.arg()
        return args
    return __protect_methods


def verify(f):

    def func(data, data0, data1, data2, data3):
        if not isinstance(data0, str):
            raise Exception
        elif not isinstance(data1, int):
            raise Exception
        elif not isinstance(data2, list):
            raise Exception
        elif not isinstance(data3, str):
            raise Exception
        return f(data, data0, data1, data2, data3)
    return func


# CREA LOS DECORADORES ARRIBA
# DESDE AQUI HACIA ABAJO NO PUEDES MODIFICAR NINGUNA DE LAS CLASES Y FUNCIONES, SOLO DECORARLAS
class Pokedex:
    def __init__(self):
        self.pokemon = list()

    @is_pokemon
    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    def compare(self):
        print('El mas fuerte es {0.nombre}'.format(
            max(self.pokemon, key=lambda x: len(x.nombre))))

    def __str__(self):
        return 'Llevas {} Pokemon:\n{}'.format(len(self.pokemon), self.pokemon)


class Pokemon:
    @verify
    def __init__(self, nombre, level, evolutions, owner):
        self.nombre = nombre
        self.level = level
        self.evolutions = evolutions
        self.owner = owner

    def set_attributes(self, tipo):
        self.tipo = tipo

    @my_name
    def __repr__(self):
        return 'Hola soy Charmander!'


class Legendario(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    try:
        pik = Pokemon('Pikachu', 32.4, ['Raichu'], 'Ash')
    except Exception:
        print('Su verify parece funcionar :)')

mag = Pokemon('Magikarp', 5, ['Gyarados'], 'Ash')
leg = Legendario('Mew', 80, [], 'Prof. Oak')
pokedex = Pokedex()

pokedex.add_pokemon('Charmander')

pokedex.add_pokemon(leg)

pokedex.add_pokemon(mag)

mag.set_attributes('Agua')
leg.set_attributes('All')

print(leg)
print(pokedex)

pokedex.compare()
