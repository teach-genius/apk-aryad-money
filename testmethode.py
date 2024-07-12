import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class HoverWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Hover Example')

    def enterEvent(self, event):
        self.set_background_color2()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.set_background_color()
        super().leaveEvent(event)

    def set_background_color(self):
        self.setStyleSheet("background-color:blue;")
    
    def set_background_color2(self):
        self.setStyleSheet("background-color:green;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HoverWidget()
    ex.show()
    sys.exit(app.exec_())
