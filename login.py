from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from registre_email import RegistreEmail
from frame1 import Frame1
from resource_path import resource_path
from settings import commandes
from operatings import login

class Login(QWidget):
    def __init__(self,parent) -> None:
        super().__init__()
        self.parent = parent
        self.centre = QWidget(self)
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
        
        self.l1 = QLineEdit(self.frame_entry)
        self.l1.setPlaceholderText("Username")
        self.l1.setStyleSheet("background-color:#545454;border-radius:10px;padding:12px;")
        self.l1.setGeometry(20, 205, 360, 40)

        self.l2 = QLineEdit(self.frame_entry)
        self.l2.setPlaceholderText("Password")
        self.l2.setStyleSheet("background-color:#545454;border-radius:10px;padding:12px;")
        self.l2.setGeometry(20, 265, 360, 40)

        registre = QLabel("<a href='#' style='color:#4BFFB3;'>Mot de passe oublié?<\a>",self.frame_entry)
        registre.setGeometry(140,315,150,30)


        btn = QPushButton("Login", self.frame_entry)
        btn.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:#3D3D3D;border-radius:10px;font-size:15px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        btn.setGeometry(20, 400, 360, 40)
        btn.clicked.connect(self.log)
        registre.setOpenExternalLinks(False)
        registre.linkActivated.connect(self.on_link_clicked)

   

    
    def barre(self):
        barre = QWidget(self.centre)
        name = QLabel(str(commandes["name_companie"]),barre)
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
        ico.setPixmap(QPixmap(resource_path('icons/16.png')).scaled(40,40))
        ico.setStyleSheet("background:transparent;padding-top:8px;padding-left:7px;padding-top:9px;")

        logo.setFixedSize(50, 50)
        logo.setStyleSheet("background-color:#545454;border-radius:22px;")
        logo.setGeometry(175, 20, 50, 50)

        titre = QLabel("Nous avons besoin de vos données\npersonnelles")
        titre.setAlignment(Qt.AlignCenter)
        titre.setStyleSheet("font-size:15px;color:#4BFFB3;")
        sous_titre = QLabel("Entrez vos informations pour vous connecter\nà votre compte.")
        sous_titre.setAlignment(Qt.AlignCenter)
        sous_titre.setStyleSheet("font-size:12px;")
        
        vue_layout.addWidget(titre)
        vue_layout.addWidget(sous_titre)

        vue.setLayout(vue_layout)
        vue.setGeometry(20, 80, 360, 110)
        vue.setStyleSheet("background-color:#3D3D3D;")

    def log(self):
            name = self.l1.text()
            pswd = self.l2.text()
            if name!="" and pswd!="":
                check= login(name,pswd) 
                if check is not None:
                    type_user= check["type_user"]
                    user_id = check["user_id"]
                    if type_user == "SuperAdmin":
                        f = Frame1(user_id,name)
                        self.parent.setframe(f)
                    else:
                        self.show_message("ERROR","Mot de passe ou nom d'utilisateur incorrect")
                else:
                   self.show_message("ERROR","Echec de connection") 
            else:
                self.show_message("ERROR","Remplissez tous les champs")

    def on_link_clicked(self):
        f = RegistreEmail(self.parent)
        self.parent.setframe(f)
    
    def show_message(self,titre,message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(titre)
        msgBox.setStyleSheet("background-color:#5B4040;color:#FF6B4B;")
        msgBox.setText(message)
        msgBox.exec()