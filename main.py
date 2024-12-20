import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QPushButton, QMainWindow

class centralwidget(QMainWindow):
    def __init__(self):
        super(centralwidget, self).__init__()
        uic.loadUi('UI.ui', self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        self.circles.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))

        for diameter in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = centralwidget()
    window.show()
    sys.exit(app.exec())