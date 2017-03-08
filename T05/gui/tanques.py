from PyQt4 import QtGui


class Tanque(QtGui.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_image()
        self.init_tank()

    def init_tank(self):
        self._cord_x = 0
        self._cord_y = 0
        self._hp = 100
        self._angle = 0
        self._max_speed = 10
        self._speed = 1
        self._mov_state = 0 #puede ir de 1 a 8

    @property
    def cord_x(self):
        return self._cord_x

    @property
    def cord_y(self):
        return self._cord_y

    @cord_x.setter
    def cord_x(self, cord):
        if cord < 5.5:
            self._cord_x = 5.5
        elif cord > 610.5:
            self._cord_x = 610.5
        else:
            self._cord_x = cord
        self.move(self.cord_x, self.cord_y)

    @cord_y.setter
    def cord_y(self, cord):
        if cord < 0:
            self._cord_y = 0
        elif cord > 224:
            self._cord_y = 224
        else:
            self._cord_y = cord
        self.move(self.cord_x, self.cord_y)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, num):
        self._angle = num

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, num):
        if num > self._max_speed:
            self._speed = self._max_speed
        elif self._speed < 0:
            print('yes')
            self._speed = 0
        else:
            self._speed += num

    @property
    def movimiento(self):
        return self._num_pix

    @movimiento.setter
    def movimiento(self, num):
        if num > 7:
            self._num_pix = 0
        else:
            self._num_pix = num

    def init_image(self):
        self.base_label = QtGui.QLabel(self)
        self.base_label.move(49, 93)
        paths0 = '1 2 3 4 5 6 7 8'.split(' ')
        paths1 = 'gui/assets/game_images/tanque/TanquePrincipal_0°_mov'
        self.pixmaps = []
        self.pixmaps = [[] for i in range(8)]
        for num in range(len(paths0)):
            for angle in range(8):
                Pixmap = QtGui.QPixmap(paths1+paths0[num]+'.png')
                Pixmap = Pixmap.scaled(33, 33)
                Pixmap = Pixmap.transformed((QtGui.QTransform().rotate(angle*45)))
                self.pixmaps[num].append(Pixmap)

        self._num_pix = 0
        self._pixmap = self.pixmaps[self._num_pix][0]
        self.base_label.setPixmap(self._pixmap)

    def rotar(self, inclinacion):
        self.angle = inclinacion // 45
        self._pixmap = self.pixmaps[self.movimiento][self.angle]
        self.base_label.setPixmap(self._pixmap)

    def move_up(self):
        self.rotar(270)
        self.cord_y -= 1*self.speed
        self.speed += 1
        self.movimiento += 1

    def move_down(self):
        self.rotar(90)
        self.cord_y += 1*self.speed
        self.speed += 1
        self.movimiento += 1

    def move_right(self):
        self.rotar(0)
        self.cord_x += 1*self.speed
        self.speed += 1
        self.movimiento += 1

    def move_left(self):
        self.rotar(180)
        self.cord_x -= 1*self.speed
        self.speed += 1
        self.movimiento += 1



