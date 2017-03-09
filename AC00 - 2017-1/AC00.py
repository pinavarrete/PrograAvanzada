import datetime


class Departamento:
    '''Clase que representa un departamento en venta
       valor esta en UF
    '''
    last_id = 0  # Variable estatica para manejar el ultimo id generado

    def __init__(self, mts2, valor, num_dorms, num_banos):
        self._id = Departamento.last_id
        self.creation_date = datetime.date.today()
        self.mts2 = mts2
        self.valor = valor
        self.num_dorms = num_dorms
        self.num_banos = num_banos
        self.vendido = False
        self._visitas = 0
        Departamento.last_id += 1

    def __str__(self):
        return ('Departamento {} ha sido visitado {} veces'
                .format(self._id, self.visitas)
                )

    @property
    def visitas(self):
        return self._visitas

    @visitas.setter
    def visitas(self, valor):
        print(
            'Has cambiado el valor de numero de visitas de {} a {}'
            .format(self._visitas, valor)
            )
        self._visitas = valor

    def vender(self):
        '''Método que simula vender el departamento
        '''
        if not self.vendido:
            self.vendido = True
        else:
            print("Departamento {} ya se vendio".format(self._id))


class PentHouse(Departamento):

    def __init__(self, mts2, valor, num_dorms, num_banos, sirvientes):
        super().__init__(mts2, valor, num_dorms, num_banos)
        self._sirvientes = sirvientes


# Main Code


d1 = Departamento(mts2=100, valor=5000, num_dorms=3, num_banos=2)
