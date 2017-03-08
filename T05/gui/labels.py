from PyQt4 import QtGui, QtCore
import sys


class QuitLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        sys.exit()

class PauseLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        print('se debería pausar')
        pass
        #aqui hay que pausar el juego

