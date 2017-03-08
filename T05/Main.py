from gui.gamewindows import GameWindow
from PyQt4 import QtGui, uic

if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = GameWindow()
    form.show()
    app.exec_()
