from PyQt4 import QtGui, QtCore, uic
from gui.tanques import Tanque
from gui.readCSV import lector_csv
from gui.labels import QuitLabel, PauseLabel


window = uic.loadUiType("gui/gamewindow.ui")

class GameWindow(window[0], window[1]):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_game()

    def init_game(self):
        self.setupUi(self)
        paths = ["gui/assets/game_images/field.jpg", "gui/assets/game_images/borde.jpg",
                 "gui/assets/menu_images/PauseButton.png", "gui/assets/menu_images/QuitButton.png"]
        piximaps = []
        for path in paths:
            piximaps.append(QtGui.QPixmap(path))
        self.pause = PauseLabel(self)
        self.quit = QuitLabel(self)
        self.pause.move(7, 8.5)
        self.quit.move(687, 8.5)
        self.pause.setPixmap(piximaps[2].scaled(42, 41))
        self.quit.setPixmap(piximaps[3].scaled(41, 41))

        #self.pause.setPixmap(piximaps[2].scaled(42, 41))
        #self.quit.setPixmap(piximaps[3].scaled(41, 41))
        self.war2.setPixmap(piximaps[0].scaled(721, 381))
        lector = lector_csv("gui/maps/Etapa1.csv")
        x, y = 18.5, 61
        for k in range(10):
            lista = next(lector)
            for iteraciones in range(len(lista)):
                if lista[iteraciones] != 'O':
                    new_label = QtGui.QLabel(self)
                    new_label.move(x, y)
                    pixmap = QtGui.QPixmap(piximaps[1])
                    pixmap = pixmap.scaled(32, 32)
                    new_label.setPixmap(pixmap)
                x += 32
            y += 32
            x = 18.5

        self.jugador = Jugador(self)
        self.jugador.start()


    def keyPressEvent(self, event):
        if event:

            if event.key() == 16777235: #Arriba
                self.jugador.jugador.move_up()

            elif event.key() == 16777237: #Abajo
                self.jugador.jugador.move_down()

            elif event.key() == 16777236: #Derecha
                self.jugador.jugador.move_right()

            elif event.key() == 16777234: #Izquierda
                self.jugador.jugador.move_left()

            elif event.text() == 'p':
                print(self.jugador.jugador.cord_x, self.jugador.jugador.cord_y)


class Jugador(QtCore.QTimer):

    def __init__(self, parent=None):
        self.jugador = Tanque(parent)
        self.jugador.base_label.show()
        super().__init__(parent)

