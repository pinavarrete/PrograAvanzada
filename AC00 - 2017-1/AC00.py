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
        self.visitas = 0
        Departamento.last_id += 1

    def __str__(self):
        return ('Departamento {} ha sido visitado {} veces'
                .format(self._id, self.visitas)
                )

    def visitar(self):
        self.visitas += 1

    def vender(self):
        '''Método que simula vender el departamento
        '''
        if not self.vendido:
            self.vendido = True
        else:
            print("Departamento {} ya se vendio".format(self._id))

# Main Code


d1 = Departamento(mts2=100, valor=5000, num_dorms=3, num_banos=2)
