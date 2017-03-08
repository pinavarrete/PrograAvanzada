from PyQt4 import QtGui
from PyQt4 import QtCore


class MiFormulario(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.texto = ''

    def init_GUI(self):
        # Creamos una etiqueta para status
        self.label1 = QtGui.QLabel('Teléfono: ', self)

        # Creamos la grilla para ubicar los Widget (botones) de manera matricial
        self.grilla = QtGui.QGridLayout()

        valores = ['Call', 'Menu', 'Off',
                   '1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '*', '0', '#']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada boton guardados en la lista valores

        posicion = [(i,j) for i in range(5) for j in range(3)]

        for posicion, valor in zip(posicion, valores):
            if valor == '':
                continue

            boton = QtGui.QPushButton(valor)

            # A todos los botones les asignamos el mismo slot o método
            boton.clicked.connect(self.boton_clickeado)

            # El * permite convertir los elementos de la tupla como argumentos
            # independientes
            self.grilla.addWidget(boton, *posicion)

        # Creamos un Layout vertical
        vbox = QtGui.QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label1)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(600, 250)
        self.setWindowTitle('CelularApp')
        self.show()

    def boton_clickeado(self):
        # En este método identificaremos el botón y la posición de este en la
        # grilla.

        # Sender retorna el objeto que fue clickeado
        boton = self.sender()

        # Obtenemos el identificador del elemento en la grilla
        idx = self.grilla.indexOf(boton)

        # Con el identificador obtenemos la posición del ítem en la grilla
        posicion = self.grilla.getItemPosition(idx)

        # Actualizamos
        if idx == 0:
            if (self.texto == '+56995485179' or self.texto == '95485179') and idx == 0:
                self.texto = 'Tio Eduardo :D'
            self.texto = 'Llamando a ' + self.texto
        elif idx == 2:
            self.texto = 'Llamada Finalizada'
        elif idx >= 3 and idx < 12:
            self.texto = self.texto + str(idx-2)
        elif idx >= 12 and idx < 14:
            if idx == 12:
                self.texto = self.texto + '+'
            elif idx == 13:
                self.texto = self.texto + '0'
        else:
            self.texto = ''

        self.label1.setText('{}'.format(self.texto))
        if idx == 2:
            self.texto = ''


if __name__ == '__main__':
    app = QtGui.QApplication([])

    # Se crea una ventana descendiente de QMainWindows
    form = MiFormulario()
    form.show()
    app.exec_()