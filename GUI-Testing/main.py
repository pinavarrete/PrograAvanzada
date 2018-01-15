import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


ui_file = uic.loadUiType('TicTacToegame.ui')


class TicTacGame(ui_file[0], ui_file[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gano = False
        self.jugadas = ['X', 'O']
        self.counter = 0

    def juego(self):
        self.counter = 0
        while self.counter < 10 and not self.gano:
            pass

    def click_button(self): caracter = self.jugadas[self.counter % 2]
    self.gridLayoutGame


if __name__ == '__main__':
    app = QApplication([])
    form = TicTacGame()
    form.show()
    sys.exit(app.exec_())
