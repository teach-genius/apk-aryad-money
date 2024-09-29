from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class FramePassWord(QWidget):
    def __init__(self,parent) -> None:
        super().__init__()
        self.parent = parent
        self.centre= QWidget(self)
        self.centre.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1,  stop: 0 #222222, stop: 1 #4BFFB3);")
        self.centre.setFixedSize(1200, 600)

        self.frame_entry = QWidget(self.centre)
        self.frame_entry.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")
        self.frame_entry.setGeometry(400,90,400,480)
        self.entry()

        self.barre()
        self.message()
        self.setFixedSize(1200, 600)


    def entry(self):
        
        l1 = QLineEdit(self.frame_entry)
        l1.setPlaceholderText("Entrez votre adresse e-mail")
        l1.setStyleSheet("background-color:#545454;border-radius:10px;padding:12px;")
        l1.setGeometry(20, 205, 360, 40)

        l2 = QLineEdit(self.frame_entry)
        l2.setPlaceholderText("Entrez un mot de passe")
        l2.setStyleSheet("background-color:#545454;border-radius:10px;padding:12px;")
        l2.setGeometry(20, 265, 360, 40)

        
        l3 = QLineEdit(self.frame_entry)
        l3.setPlaceholderText("Confirmez le mot de passe")
        l3.setStyleSheet("background-color:#545454;border-radius:10px;padding:12px;")
        l3.setGeometry(20, 325, 360, 40)

        btn = QPushButton("Login", self.frame_entry)
        btn.setStyleSheet("background-color:#4BFFB3;color:#3D3D3D;border-radius:10px;font-size:15px;font:bold;")
        btn.setGeometry(20, 400, 360, 40)
       
    
    def barre(self):
        barre = QWidget(self.centre)
        name = QLabel("AryadMoney",barre)
        name.setStyleSheet("font-size:18px;font:bold;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        name.setGeometry(100,8,150,30)
        aide = QPushButton("?",barre)
        aide.setGeometry(1150,12,20,20)
        aide.setStyleSheet("background-color:#4BFFB3;color:#3D3D3D;font-size:20px;border-radius:10px;")

        barre.setGeometry(0, 0, 1200, 45)
        barre.setStyleSheet("background-color:#2E2E2E;")
    
    def message(self):
        vue = QWidget(self.frame_entry)
        vue_layout = QVBoxLayout()
        vue_layout.setAlignment(Qt.AlignCenter)

        logo = QLabel(self.frame_entry)
        ico = QLabel(logo)
        ico.setPixmap(QPixmap(r"Frames\icons\15.png").scaled(35,35))
        ico.setStyleSheet("background:transparent;padding-top:8px;padding-left:7px;")

        logo.setFixedSize(50, 50)
        logo.setStyleSheet("background-color:#545454;border-radius:22px;")
        logo.setGeometry(175, 20, 50, 50)

        titre = QLabel("Saisis les informations de ton\ncompte")
        titre.setAlignment(Qt.AlignCenter)
        titre.setStyleSheet("font-size:20px;color:#4BFFB3;")
        sous_titre = QLabel("Dernière étape ! Crée ton mot de passe pour\nfinaliser l'inscription")
        sous_titre.setAlignment(Qt.AlignCenter)
        sous_titre.setStyleSheet("font-size:12px;")
        
        vue_layout.addWidget(titre)
        vue_layout.addWidget(sous_titre)

        vue.setLayout(vue_layout)
        vue.setGeometry(20, 80, 360, 110)
        vue.setStyleSheet("background-color:#3D3D3D;")

    
        

