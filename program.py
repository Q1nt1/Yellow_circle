import sys
from random import randrange

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setFixedSize(600, 600)
        self.do_paint = False
        self.btn = QPushButton('Clicked', self)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        d = randrange(1, 600)
        x = randrange(-600, 600)
        y = randrange(-600, 600)
        qp.setBrush(QColor(randrange(0, 255), randrange(10, 255), randrange(0, 255)))
        qp.setPen(QColor(0, 0, 0))
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
