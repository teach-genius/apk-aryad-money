from PySide6.QtWidgets import QApplication, QMainWindow
from login import Login
from settings import commandes

#page de connexion
class Connexion(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.central_widget = Login(self)
        self.setFixedSize(1200, 600)
        self.setWindowTitle(str(commandes["main_window_title"]))
        self.setframe(self.central_widget)
    def setframe(self, fen):
        self.setCentralWidget(fen)

if __name__ == "__main__":
    app = QApplication([])
    window = Connexion()
    window.show()
    app.exec()