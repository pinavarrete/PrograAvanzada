from collections import defaultdict


# __len__


class MyLista(list):
    def __len__(self):

        # Cada vez que se llame con un key que no existe, se genera como default el valor 0,
        # que sale de llamar a "int" sin argumentos (probar tipeando int() en la consola de Python).

        d = defaultdict(int)
        for i in range(list.__len__(self)):  # aquí llamamos a la función len de la clase list
            d.update({self[i]: d[self[i]] + 1})

        # aquí se llama al método len de d, que es un defaultdict
        return len(d)


L = MyLista([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
# print(len(L))


# Otra forma de hacer lo mismo
class MyLista2(list):
    def __len__(self):
        # cada vez que se llame con un key que no existe, se genera como default el valor 0,
        # que sale de llamar a "int" sin argumentos (probar tipeando int() en la consola de Python).
        d = defaultdict(int)
        for i in self:  # aquí llamamos a la función len de la clase list
            d.update({i: d[i] + 1})
        return len(d)  # aquí se llama al método len de d, que es un defaultdict


L = MyLista2([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
# print(len(L))


# Otra forma de hacer lo mismo
class MyLista3(list):
    def __len__(self):
        d = set(self)
        return len(d)  # aquí se llama al método len de d, que es un defaultdict


L = MyLista3([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
# print(len(L))


# __getitem__
class MiClase:
    def __init__(self, palabra=None):
        self.palabra = palabra

    def __getitem__(self, i):
        return self.palabra[i]


p = MiClase("hola_mundo")
# print(p[0])

# [print(c) for c in p]

(a, b, c, d) = p[0:4]
# print(a, b, c, d)
# print(list(p))
# print(tuple(p))


# __reversed


lista = [1, 2, 3, 4, 5, 6]


class MiSecuencia:
    # Como en esta clase no estamos haciendo overriding del método __reversed__, simplemente se
    # usará el built-in, que iterará usando __getitem__ y __len__
    def __len__(self):
        return 9

    def __getitem__(self, index):
        return "Item_{0}".format(index)


class MiReversa(MiSecuencia):
    def __reversed__(self):
        return "Reversando!!"


for seq in lista, MiSecuencia(), MiReversa():
    # print("\n{} : ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        # print(item, end=", ")
        pass

# Enumerate


lista = ["a", "b", "c", "d"]

for i, j in enumerate(lista):
    # print("{}: {}".format(i, j))
    pass

# print([par for par in enumerate(lista)])

# Aquí creamos un diccionario con el indice entregado por enumerate usado como key
# print({i: j for i, j in enumerate(lista)})

# Zip


variables = ['nombre', 'apellido', 'email']
p1 = ["Juan", 'Perez', 'jp1@hotmail.com']
p2 = ["Gonzalo", 'Aldunate', 'gan@gmail.com']
p3 = ["Alberto", 'Gomez', 'agomez@yahoo.com']

contactos = []
for p in p1, p2, p3:
    contacto = zip(variables, p)
    contactos.append(dict(contacto))

for c in contactos:
    #  El doble asterisco es para pasar el diccionario c como "keyworded" argumentos
    # es equivalente a .format(nombre = c["nombre"], apellido = c["apellido"], email = c["email"]
    # print("Nombre: {nombre} {apellido}, email: {email}".format(**c))
    pass

# print(list(zip(variables, p1, p2, p3)))

A = [1, 2, 3, 4]
B = ['a', 'b', 'c', 'd']

# print(*A)
# print(*B)

zipped = zip(A, B)
zipped = list(zipped)
# print(zipped)

unzipped = zip(*zipped)
unzipped = list(unzipped)
# print(unzipped)


# Listas por comprension


lista = ['1', '4', '55', '65', '4', '15', '90']
int_lista = [int(c) for c in lista]
# print(int_lista)

int_lista_2d = [int(c) for c in lista if len(c) > 1]
# print(int_lista_2d)

secuencia = ["one", "two", "three"]

s2 = ['%d: %s' % (i, j) for i, j in enumerate(secuencia)] # estilo antiguo de formateo del print

# print(s2)


# Sets y Diccionarios por comprension

from collections import namedtuple
# namedtuple es una subclase de tuplas que tiene campos (con nombres arbitrarios),
# pueden ser accesados como tupla.campo
Peli = namedtuple("Pelicula", ["titulo", "director", "genero"])
peliculas = [Peli("Into the Woods", "Rob Marshall", "Adventure"),
             Peli("American Sniper", "Clint Eastwood", "Action"),
             Peli("Birdman", "Alejandro González Inárritu", "Comedy"),
             Peli("Boyhood", "Richard Linklater", "Drama"),
             Peli("Taken 3", "Olivier Megaton", "Action"),
             Peli("The Imitation Game", "Morten Tyldum", "Biography"),
             Peli("Gone Girl", "David Fincher", "Drama")]

directores_accion = {b.director for b in peliculas if b.genero == 'Action'}  # set comprehension
# print(directores_accion)

dict_directores_accion = {b.director: b for b in peliculas if b.genero == 'Action'}
# print(dict_directores_accion)

# print(dict_directores_accion['Olivier Megaton'])


# Iterables e Iteradores


x = [11, 32, 43]
# for c in x: print(c)
# print(x.__iter__)
try:
    next(x)  # aqui podemos ver que una lista no es un iterador
except Exception as err:
    pass
    # print(err)

y = iter(x)
# print(next(y))
# print(next(y))
# print(next(y))


class Carta:
    MONOS = {11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self, numero, pinta):
        self.pinta = pinta
        self.numero = numero if numero <= 10 else Carta.MONOS[numero]

    def __str__(self):
        return "%s %s" % (self.numero, self.pinta)


class Baraja:
    def __init__(self):
        self.cartas = [Carta(n, p) for p in ['Espada', 'Diamante', 'Corazon', 'Trebol'] for n in range(1, 14)]

        # La lista por comprension equivale a escribir:
        # self.cartas = []
        # for p in ['Espada', 'Diamante', 'Corazon', 'Trebol']:
        #    for n in range(1, 14):
        #        self.cartas.append(Carta(n, p))


# for c in Baraja().cartas: print(c)

class Baraja():
    def __init__(self):
        self.cartas = [Carta(n, p) for p in ['Espada', 'Diamante', 'Corazon', 'Trebol'] for n in range(1, 14)]

    def __iter__(self):
        return iter(self.cartas)

# for c in Baraja(): print(c)


b = iter(Baraja())
# for i in range(6): print(next(b))


class Fib:
    def __init__(self):
        self.prev = 0
        self.actual = 1

    def __iter__(self):
        return self

    def __next__(self):
        valor = self.actual
        self.actual += self.prev
        self.prev = valor
        return valor


f = Fib()
N = 10
l = [next(f) for i in range(N)]
# print(l)


import itertools

letras = ['a', 'b', 'c', 'd', 'e', 'f']
bools = [1, 0, 1, 0, 0, 1]
nums = [23, 20, 44, 32, 7, 12]
decimales = [0.1, 0.7, 0.4, 0.4, 0.5]

colors = itertools.cycle(letras)
# for i in range(10): print(next(colors))

# for i in itertools.chain(letras, bools, decimales): print(i, end=" ")
# print()
# for i in itertools.compress(letras, bools): print(i, end=" ")


# Generadores

from sys import getsizeof
a = (b for b in range(10))#por el sólo hecho de usar paréntesis significa que estamos creando un generador
print(sum(a))
print(getsizeof(a))
c = [b for b in range(10)]#c usa más memoria que a
print(getsizeof(c))
for b in a: print(b)
print(sum(a))#como ya terminamos de iterar sobre a, la secuencia desaparece
