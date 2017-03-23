class Arbol:
    # Creamos la estructura básica del árbol. Los nodos hijos pueden ser guardados en alguna
    # estructura como listas o diccionarios. Sin pérdidad de generalidad, en este ejemplo los
    # nodos hijos serán guardados en un diccionario.

    def __init__(self, id_nodo, valor=None, id_padre=None):
        self.id_nodo = id_nodo
        self.id_padre = id_padre
        self.valor = valor
        self.hijos = {}

    def agregar_nodo(self, id_nodo, valor=None, id_padre=None):
        # Cada vez que agregamos un nodo verificamos primero si corresponde al nodo padre
        # donde queremos agregar el nuevo nodo. Si no es el nodo, buscamos recursivamente
        # a través de todos los nodos existentes hasta que encontremos el nodo correspondiente.

        if self.id_nodo == id_padre:
            # Si el nodo es el nodo padre, entonces actualizamos el diccionario
            # con los hijos

            self.hijos.update({id_nodo: Arbol(id_nodo, valor, id_padre)})

        else:
            # Si no, recursivamente seguimos buscando en el árbol el nodo padre

            for hijo in self.hijos.values():
                hijo.agregar_nodo(id_nodo, valor, id_padre)

    def obtener_nodo(self, id_nodo):
        # recursivamente obtenemos el nodo siempre y cuando exista la posicion.

        if self.id_nodo == id_nodo:
            return self
        else:
            for hijo in self.hijos.values():
                nodo = hijo.obtener_nodo(id_nodo)

                if nodo:
                    # retorna el nodo si es que existe en el árbol
                    return nodo

    def __repr__(self):
        # Para visualizar el arbol redefinimos el método __repr__ para recorrer recursivamente
        # todos los nodos del árbol.

        def recorrer_arbol(raiz):
            for hijo in raiz.hijos.values():
                self.ret += "id-nodo: {} -> id_padre: {} -> valor: {}\n".format(hijo.id_nodo, hijo.id_padre, hijo.valor)
                recorrer_arbol(hijo)

            return self

        self.ret = 'RAIZ:\nroot-id: {} -> valor: {}\n\nHIJOS:\n'.format(self.id_nodo, self.valor)
        recorrer_arbol(self)
        return self.ret

T = Arbol(0, 10)
T.agregar_nodo(1, 8, 0)
T.agregar_nodo(2, 12, 0)
T.agregar_nodo(3, 4, 1)
T.agregar_nodo(4, 9, 1)
T.agregar_nodo(5, 1, 3)
T.agregar_nodo(6, 18, 2)

# Desplegamos el árbol según se definió en el método __repr__
print(T)
