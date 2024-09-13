from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtPrintSupport import *
from datetime import datetime
import locale
from settings import *
from operatings import *
import re
import secrets
import string
import random
from PySide6.QtPrintSupport import *
import os 
import random
import string
import webbrowser

class History(QWidget):
    def __init__(self) -> None:
        super().__init__()


class Frame1(QWidget):
    def __init__(self,code_user,name) -> None:
        super().__init__()
        self.infoapk = commandes
        self.setStyleSheet("background-color:#2E2E2E;")
        self.setFixedSize(1200, 600)
        self.declaration(code_user)
        self.layout = QHBoxLayout()
        self.nameuserconnect = name
        self.lateral()
        self.central()
        self.setLayout(self.layout)
        self.code_user = None
        self.setcodeuser(code_user)
    
    def setcodeuser(self,new_code):
        self.code_user = new_code
       
    def lateral(self):
        self.panel_lateral = QWidget()
        self.panel_lateral.setFixedWidth(230)
        self.panel_lateral.setStyleSheet("background-color: #2E2E2E;border-radius:10px;")
        self.btnconnect()
        self.layout.addWidget(self.panel_lateral)
    
    def btnconnect(self):
        layout_btn = QVBoxLayout()
        box1 = QWidget()
        layout2 = QVBoxLayout()
        w1 = QWidget()
        logo = QLabel(w1)
        logo.setPixmap(QPixmap(r"Frames\icons\logo.png").scaled(30,26))
        logo.setGeometry(10,8,30,25)
       
        
        name_logoU = QLabel("AryadMoney", w1)
        name_logoU.setGeometry(55, 8, 150, 25)
        name_logoU.setStyleSheet("font-size:18px;font:bold;color:#808080;font-weight: bold;")

        w1.setFixedHeight(40)
        w1.setStyleSheet("background-color:#2E2E2E;")
        w2 = QWidget()
        logow2 = QLabel(w2)
        logow2.setStyleSheet("border:0px;")
        logow2.setPixmap(QPixmap(r"Frames\icons\user_1077114.png").scaled(24,24))
        logow2.setGeometry(10,8,24,24)
        
        unc = QLabel(w2)
        unc.setText(f'<span>~</span>Bonjour,{self.nameuserconnect}<span>~</span>')
        unc.setGeometry(55,8,230,24)
        unc.setStyleSheet("font:bold;")
        
        w2.setFixedHeight(40)
        w2.setStyleSheet("background-color:#2E2E2E;")
        layout2.addWidget(w1)
        layout2.addWidget(w2)

        box1.setLayout(layout2)
        box1.setFixedHeight(100)
        

        box2 = QWidget()
        box2.setFixedHeight(250)
        layout = QVBoxLayout()

        box3 = QWidget()
        bx3_layout =QVBoxLayout()


        self.b1 = QWidget()
        self.b1.setStyleSheet("background-color:#4BFFB3;")
        lb1_layout = QHBoxLayout()
        lb1 = QLabel("Acceuil")
        lb1.setStyleSheet("color:#808080;font-weight: bold;")
        ico_drach = QPushButton()
        ico_drach.clicked.connect(self.Acceuil)
        ico_drach.setIcon(QIcon(QPixmap(r"Frames\icons\home.png").scaled(30, 30)))  # Ajout de l'icône correctement
        lb1_layout.addWidget(ico_drach)
        lb1_layout.addWidget(lb1)
        self.b1.setLayout(lb1_layout)
        self.b1.setFixedHeight(45)
        self.selected =self.b1

        self.b2 = QWidget()
        lb2_layout = QHBoxLayout()
        lb2 = QLabel("Transactions")
        lb2.setStyleSheet("color:#808080;font-weight: bold;")
        ico_inv = QPushButton()
        ico_inv.clicked.connect(self.invoivepanel)
        ico_inv.setIcon(QIcon(QPixmap(r"Frames\icons\transaction.png").scaled(30, 30)))
        lb2_layout.addWidget(ico_inv)
        lb2_layout.addWidget(lb2)
        self.b2.setLayout(lb2_layout)
        self.b2.setFixedHeight(45)

        self.b3 = QWidget()
        lb3_layout = QHBoxLayout()
        lb3 = QLabel("Carte")
        lb3.setStyleSheet("color:#808080;font-weight: bold;")
        ico_card= QPushButton()
        ico_card.clicked.connect(self.cardpanel)
        ico_card.setIcon(QIcon(QPixmap(r"Frames\icons\19.png").scaled(30, 30)))
        lb3_layout.addWidget(ico_card)
        lb3_layout.addWidget(lb3)
        self.b3.setLayout(lb3_layout)
        self.b3.setFixedHeight(45)

        self.b4 = QWidget()
        lb4_layout = QHBoxLayout()
        lb4 = QLabel("Historique")
        lb4.setStyleSheet("color:#808080;font-weight: bold;")
        ico_history = QPushButton()
        ico_history.clicked.connect(self.Historique)
        ico_history.setIcon(QIcon(QPixmap(r"Frames\icons\20.png").scaled(30, 30)))  # Ajout de l'icône correctement
        lb4_layout.addWidget(ico_history)
        lb4_layout.addWidget(lb4)
        self.b4.setLayout(lb4_layout)
        self.b4.setFixedHeight(45)
        
        self.b5 = QWidget()
        lb5_layout = QHBoxLayout()
        lb5 = QLabel("Parametre")
        lb5.setStyleSheet("color:#808080;font-weight: bold;")
        ico_setting = QPushButton()
        ico_setting.clicked.connect(self.parametrepanel)
        ico_setting.setIcon(QIcon(QPixmap(r"Frames\icons\22.png").scaled(30, 30)))
        lb5_layout.addWidget(ico_setting)
        lb5_layout.addWidget(lb5)
        self.b5.setLayout(lb5_layout)
        self.b5.setFixedHeight(45)

        b6 = QWidget()
        b6.setStyleSheet("background-color:#4BFFB3;")
        lb6_layout = QHBoxLayout()
        lb6 = QLabel("Sortir")
        lb6.setStyleSheet("color:#808080;font-weight: bold;")
        ico_exit = QPushButton()
        ico_exit.clicked.connect(QApplication.instance().quit)
        ico_exit.setIcon(QIcon(QPixmap(r"Frames\icons\exit.png").scaled(30, 30)))
        lb6_layout.addWidget(ico_exit)
        lb6_layout.addWidget(lb6)
        b6.setLayout(lb6_layout)
        b6.setFixedHeight(45)

        bx3_layout.addWidget(b6)
        box3.setLayout(bx3_layout)

        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        layout.addWidget(self.b3)
        layout.addWidget(self.b4)
        layout.addWidget(self.b5)
        box2.setLayout(layout)

        layout_btn.addWidget(box1)
        layout_btn.addWidget(box2)
        layout_btn.addWidget(box3)
        self.panel_lateral.setLayout(layout_btn)

    def central(self):
        self.panel_central = QWidget()
        self.panel_central_layout = QVBoxLayout()
        self.panel_central.setStyleSheet("background-color: #2E2E2E")
        self.panel_central_layout.addWidget(self.sous_panel_central_top)
        self.panel_central_layout.addWidget(self.sous_panel_central_central)
        self.panel_central.setLayout(self.panel_central_layout)
        self.layout.addWidget(self.panel_central)
        self.old_wid = self.panel_central

    def Historique(self):
        self.selectionOption(self.b4)
        panel_top =QWidget()
        panel_top.setFixedHeight(80)

        lh1 = QHBoxLayout()
        wh1 = QWidget(panel_top)
        wh1.setGeometry(10,0,145,36)
        wh1.setFixedWidth(125)

        date_icon = QLabel()
        date_icon.setPixmap(QPixmap(r"Frames\icons\fleche.png").scaled(24,24))
        # Définir la locale pour afficher la date en français
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
        date =datetime.now().date()
        date = date.strftime("%d %B %Y")
        text_date = QLabel(str(date))
        lh1.addWidget(date_icon)
        lh1.addWidget(text_date)
        wh1.setLayout(lh1)
        



        notif = QPushButton(panel_top)
        notif.setGeometry(550,0,36,36)
        notif.setIcon(QIcon(QPixmap(r"Frames\icons\18.png")))
        notif.setFixedSize(36,36)
        notif.setStyleSheet("background-color:transparent;")
        
        sear_wid = QWidget(panel_top)
        sear_wid.setGeometry(628,0,300,40)
        sear_wid.setStyleSheet("border-radius:12px;background-color:#D9D9D9;")
        sear_wid.setFixedSize(300,40)
        lay_h2 = QHBoxLayout()
        edit_search = QLineEdit()
        edit_search.setStyleSheet("color:black;")
        edit_search.setPlaceholderText("search here")
        btn_search = QPushButton()
        btn_search.setIcon(QIcon(QPixmap(r"Frames\icons\icon5.png")))
        lay_h2.addWidget(edit_search)
        lay_h2.addWidget(btn_search)
        sear_wid.setLayout(lay_h2)


#########################################
        panel_transaction = QWidget()
        layout_transaction =QVBoxLayout()

        tit_hit = QLabel("Historique Transaction")
        tit_hit.setStyleSheet("font-size:22px;margin-left:10px;font-weight: bold;")
        
        choice_wid = QWidget()
        choice_wid.setFixedWidth(170)
        choice_lay = QHBoxLayout()

        alltext = QPushButton("All")
        alltext.setStyleSheet("color:red;")
        
        alltext.clicked.connect(self.historiquerall)
        
        depotext = QPushButton("Envoie")
        depotext.clicked.connect(self.historiquesend)
        
        retrait = QPushButton("Retrait")
        retrait.clicked.connect(self.historiqueretrait)
        
        alltext.setStyleSheet("background-color:transparent;font-size:16px;")
        depotext.setStyleSheet("background-color:transparent;font-size:16px;")
        retrait.setStyleSheet("background-color:transparent;font-size:16px;")

        choice_lay.addWidget(alltext)
        choice_lay.addWidget(depotext)
        choice_lay.addWidget(retrait)
        choice_wid.setLayout(choice_lay)

        view_historique = QWidget()

        titles_layout = QHBoxLayout()
        titles_win = QWidget(view_historique)
        liste = ["Nature Transaction","Date Transaction","Solde Transaction","Emetteur","Recepteur","Frais Transaction","Pays Emission"]
        for i in liste:
            l = QLabel(i)
            l.setStyleSheet("font:bold;font-size:10px;")
            titles_layout.addWidget(l)
        titles_win.setLayout(titles_layout)
        titles_win.setGeometry(20,0,910,40)

        view_historique.setFixedHeight(380)
        self.History_scrolarea = QScrollArea(view_historique)
        
        tab_fram= self.chargeHistorique() 

        self.History_scrolarea.setWidget(tab_fram)
        self.History_scrolarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.History_scrolarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.History_scrolarea.setWidgetResizable(True)
        self.History_scrolarea.setGeometry(10,39,910,330)
        
        view_historique.setStyleSheet("background:#3D3D3D;border-radius:15px;")
        layout_transaction.addWidget(panel_top)
        layout_transaction.addWidget(tit_hit)
        layout_transaction.addWidget(choice_wid)
        layout_transaction.addWidget(view_historique)
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color: #2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)
    
    def historiquesend(self):
        self.updateHistoryView("envoie")
       
    def historiqueretrait(self):
        self.updateHistoryView("retrait")
       
    def historiquerall(self):
        self.updateHistoryView("All")
       
    def updateHistoryView(self, vue):
        if vue=="All":
            tab_fram = self.chargeHistorique()
            if tab_fram is not None:
                self.History_scrolarea.setWidget(tab_fram)
        else:      
            tab_fram = self.chargeHistorique2(vue)
            if tab_fram is not None:
                self.History_scrolarea.setWidget(tab_fram)
            

    def Acceuil(self):
        self.selectionOption(self.b1)
        self.replace_widget(self.old_wid,self.panel_central)
    
    def parametrepanel(self):
        self.selectionOption(self.b5)
        panel_transaction = QWidget()
        layout_transaction =QVBoxLayout()
        layout_transaction.addWidget(QWidget())
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color: #2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)
    
    def cardpanel(self):
        self.selectionOption(self.b3)
        panel_transaction = QWidget()
        layout_transaction =QHBoxLayout()
        
        
        vleft = QWidget()
        vleft.setFixedWidth(300)
        vleftlayout = QVBoxLayout()
        
        labnom = QLabel()
        labnom.setText('<span style="color:red;">*</span><span style="color:white;"> Nom</span>')
        self.balncelft1 = QLineEdit(vleft)
        self.balncelft1.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft1.setPlaceholderText("Nom")
        self.balncelft1.setFixedHeight(30)
        
        labprenom = QLabel()
        labprenom.setText('<span style="color:red;">*</span><span style="color:white;"> Prenom</span>')
        self.balncelft2 = QLineEdit(vleft)
        self.balncelft2.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft2.setPlaceholderText("Prenom")
        self.balncelft2.setFixedHeight(30)
        
        labpays = QLabel()
        tab_cfa = ["Pays","Maroc","Gabon"]
        labpays.setText('<span style="color:red;">*</span><span style="color:white;"> Pays</span>')
        self.balncelft3 = QComboBox(vleft)
        self.balncelft3.addItems(tab_cfa)
        self.balncelft3.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft3.setPlaceholderText("Pays")
        self.balncelft3.setFixedHeight(30)
        
        self.balncelft3.currentIndexChanged.connect(self.on_combobox_change)
        
        labville = QLabel()
        labville.setText('<span style="color:red;">*</span><span style="color:white;"> Ville</span>')
        self.balncelft4 = QComboBox(vleft)
        self.balncelft4.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft4.setPlaceholderText("Ville")
        self.balncelft4.setFixedHeight(30)
        
        labcni = QLabel()
        labcni.setText('<span style="color:red;">*</span><span style="color:white;"> CNI</span>')
        self.balncelft5 = QLineEdit(vleft)
        self.balncelft5.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft5.setPlaceholderText("CNI")
        self.balncelft5.setFixedHeight(30)
       
        labphone = QLabel()
        labphone.setText('<span style="color:red;">*</span><span style="color:white;"> Telephone</span>')
        self.balncelft6 = QLineEdit(vleft)
        self.balncelft6.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft6.setPlaceholderText("Telephone")
        self.balncelft6.setFixedHeight(30)
        
        labemail = QLabel()
        labemail.setText('<span style="color:red;">*</span><span style="color:white;"> Email</span>')
        self.balncelft7 = QLineEdit(vleft)
        self.balncelft7.setStyleSheet("border-radius:4px;background-color:#ffffff;padding-left:12px;color:black;")
        self.balncelft7.setPlaceholderText("Email")
        self.balncelft7.setFixedHeight(30)
        
        inf = QLabel("Informations de l'utilisateur")
        inf.setStyleSheet("margin-left:60px;margin-bottom:5px;font-weight: bold;")
        vleftlayout.addWidget(inf)
        vleftlayout.addWidget(labnom)
        vleftlayout.addWidget(self.balncelft1)
        vleftlayout.addWidget(labprenom)
        vleftlayout.addWidget(self.balncelft2)
        vleftlayout.addWidget(labpays)
        vleftlayout.addWidget(self.balncelft3)
        vleftlayout.addWidget(labville)
        vleftlayout.addWidget(self.balncelft4)
        vleftlayout.addWidget(labcni)
        vleftlayout.addWidget(self.balncelft5)
        vleftlayout.addWidget(labphone)
        vleftlayout.addWidget(self.balncelft6)
        vleftlayout.addWidget(labemail)
        vleftlayout.addWidget(self.balncelft7)
        vleft.setLayout(vleftlayout)
        vleft.setStyleSheet("background-color:#3D3D3D;border-radius:15px")
        layout_transaction.addWidget(vleft)
        
        vright = QWidget()
        vright.setStyleSheet("background-color:#3D3D3D;border-radius:15px")
       
        saveclient = QPushButton("Enregistrer client", vright)
        iconsc = QIcon(QPixmap(r"Frames\icons\add-friend_2198124.png"))
        saveclient.setIcon(iconsc)
        saveclient.clicked.connect(self.createuser)
        saveclient.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        saveclient.setGeometry(5,525,150,30)
        
        createcard = QPushButton("Créer compte MAD",vright)
        iconcc = QIcon(QPixmap(r"Frames\icons\business_16576723.png"))
        createcard.setIcon(iconcc)
        createcard.clicked.connect(self.createmadaccount)
        createcard.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        createcard.setGeometry(159,525,150,30)
        
        createcardf = QPushButton("Créer compte FCFA",vright)
        iconcc1 = QIcon(QPixmap(r"Frames\icons\business_16576723.png"))
        createcardf.setIcon(iconcc1)
        createcardf.clicked.connect(self.createfcfaaccount)
        createcardf.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        createcardf.setGeometry(313,525,150,30)
        
        grdh = QGroupBox("création de compte MAD",vright)
        grdh.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.choix1 = QRadioButton("Actif",grdh)
        choix2 = QRadioButton("Inactif",grdh)
        self.choix1.setChecked(True)
        grdh.setGeometry(10,10,300,150)
        self.choix1.setGeometry(10,20,150,50)
        choix2.setGeometry(80,20,150,50)
        
        grfcfa = QGroupBox("création de compte FCFA",vright)
        grfcfa.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.choix1f = QRadioButton("Actif",grfcfa)
        choix2f = QRadioButton("Inactif",grfcfa)
        self.choix1f.setChecked(True)
        grfcfa.setGeometry(200,10,300,150)
        self.choix1f.setGeometry(10,20,150,50)
        choix2f.setGeometry(80,20,150,50)
        
        view_mod = QLabel(vright)
        view_mod.setGeometry(550,20,50,50)
        view_mod.setPixmap(QPixmap(r"Frames\icons\connection_12061681.png").scaled(50,50))
         
        sec = QWidget(vright)
        
        usern = QLabel(sec)
        usern.setText('<span style="color:red;">*</span><span style="color:white;"> Nom utilisateur</span>')
        usern.setGeometry(10,50,230,30)
        
        self.username_sec = QComboBox(sec)
        self.username_sec.setPlaceholderText("Nom utilisateur")
        self.username_sec.setFixedHeight(30)
        self.username_sec.setStyleSheet("background-color:#ffffff;color:black;padding-left:12px;border-radius:4px;")
        self.getallusers(self.username_sec)
        
        labpass = QLabel(sec)
        labpass.setText('<span style="color:red;">*</span><span style="color:white;"> Mot de passe</span>')
        labpass.setGeometry(10,110,230,30)
        
        self.password_sec = QLineEdit(sec)
        self.password_sec.setPlaceholderText("Mot de passe par defaut")
        self.password_sec.setFixedHeight(30)
        self.password_sec.setStyleSheet("background-color:#ffffff;color:black;padding-left:12px;border-radius:4px;")
        
        self.generated  = QCheckBox("Generer le mot de passe",sec)
        self.generated.setGeometry(10,175,230,30)
        self.generated.clicked.connect(self.genered)
        
        items = ["Doit d'accès","SuperAdmin","Admin","FL","Client"]
        self.user_type_sec = QComboBox(sec)
        self.user_type_sec.addItems(items)
        self.user_type_sec.setPlaceholderText("Droit d'accès")
        self.user_type_sec.setFixedHeight(30)
        self.user_type_sec.setStyleSheet("background-color:#ffffff;color:black;padding-left:12px;border-radius:4px;")
        
        self.activation_code_sec = QLineEdit(sec)
        self.activation_code_sec.setFixedHeight(30)
        self.activation_code_sec.setPlaceholderText("Code d'activation")
        self.activation_code_sec.setStyleSheet("background-color:#ffffff;color:black;padding-left:12px;border-radius:4px;")
        
        self.generated_code = QCheckBox("Generer code d'activation",sec)
        self.generated_code.clicked.connect(self.generatednum)
        
        gpr = QGroupBox("status de securité du compte ",sec)
        gpr.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.actifac = QRadioButton("Actif",sec)
        self.inactifac = QRadioButton("Inactif",sec)
        self.inactifac.setChecked(True)
        gpr.setGeometry(0,340,230,30)
        self.actifac.setGeometry(10,365,230,30)
        self.inactifac.setGeometry(80,365,230,30)
        
        savacces = QPushButton("Enregistre permissions",vright)
        icop = QIcon(QPixmap(r"Frames\icons\account_4291647.png"))
        savacces.setIcon(icop)
        savacces.clicked.connect(self.create_security_privilege)
        savacces.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        savacces.setGeometry(467,525,150,30)
        
        priv = QLabel("Privilèges utilisateur",sec)
        priv.setStyleSheet("color:#ffffff;font-weight: bold;")
        priv.setGeometry(65,10,230,30)
            
        self.username_sec.setGeometry(10,80,230,30)
        self.password_sec.setGeometry(10,140,230,30)
        self.user_type_sec.setGeometry(10,210,230,30)
        dt = QLabel(sec)
        dt.setText('<span style="color:red;">*</span><span style="color:white;"> Code activation</span>')
        dt.setStyleSheet("background-color:transparent;")
        dt.setGeometry(10,240,230,30)
        self.activation_code_sec.setGeometry(10,270,230,30)
        self.generated_code.setGeometry(10,305,230,30)
    
        sec.setStyleSheet("background-color:#2E2E2E;")
        sec.setGeometry(360,80,250,420)
        
        layout_transaction.addWidget(vright)
        
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color:#2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)
        
        card_view = QWidget(vright)
        card_view.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1, stop:0#4BFF93,stop:1#32A528);")

        puc = QLabel(card_view)
        puc.setPixmap(QPixmap(r"Frames\icons\puce.png").scaled(47,37))
        puc.setGeometry(45,80,47,37)

        pp = QLabel(card_view)
        pp.setPixmap(QPixmap(r"Frames\icons\ppu.png").scaled(32,32))
        pp.setGeometry(10,82,32,32)
        pp.setStyleSheet("background-color:transparent;")

        self.nameuser1 = QComboBox(card_view)
        self.nameuser1.setStyleSheet("font:bold;background-color:#ffffff;border-radius:4px;color:black;")
        self.nameuser1.setPlaceholderText("Nom utilisateur")
        self.nameuser1.setGeometry(170,10,150,30)
        
        self.id_card2  = QLabel("ID:",card_view)
        self.id_card2.setStyleSheet("padding-left:6px;font-weight: bold;")
        self.id_card2.setGeometry(10,160,30,30)
        
        lbcard2 = QLabel(card_view)
        lbcard2.setGeometry(170,55,100,100)
        lbcard2.setStyleSheet("background-color:transparent;")
        lbcard2.setPixmap(QPixmap(r"Frames\icons\deposit_9334619.png").scaled(100,100))
        
        
        self.view_id_card2 = QLineEdit(card_view)
        self.view_id_card2.setEnabled(False)
        self.view_id_card2.setStyleSheet("font-size:20px;border-radius:0px;background-color:transparent;color:#ffffff;padding-left:12px;font:bold;")
        self.view_id_card2.setGeometry(30,160,230,30)
        
        card_view.setGeometry(10,80,340,200)
        
        
        self.check_id_card = QCheckBox("Generer ID de la carte FCFA",vright)
        self.check_id_card.setGeometry(20,281,340,19)
        self.check_id_card.clicked.connect(self.generedIDFCFA)
        
        self.check_id_card2 = QCheckBox("Generer ID de la carte MAD",vright)
        self.check_id_card2.setGeometry(20,503,340,19)
        self.check_id_card2.clicked.connect(self.generedIDMAD)
        
        card_view1 = QWidget(vright)
        card_view1.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1,  stop: 0 #284AA5, stop: 1 #4B7DFF);")

        self.nameuser = QComboBox(card_view1)
        self.nameuser.setStyleSheet("font:bold;background-color:#ffffff;border-radius:4px;color:black;")
        self.nameuser.setPlaceholderText("Nom utilisateur")
        self.nameuser.setGeometry(170,10,150,30)
        
        self.getallusers(self.nameuser)
        self.getallusers(self.nameuser1)
        
        self.id_card1  = QLabel("ID:",card_view1)
        self.id_card1.setStyleSheet("padding-left:6px;font-weight: bold;")
        self.id_card1.setGeometry(10,160,30,30)
        
        puce2 = QLabel(card_view1)
        puce2.setPixmap(QPixmap(r"Frames\icons\puce.png").scaled(47,37))
        puce2.setGeometry(45,80,47,37)
        
        lbcard1 = QLabel(card_view1)
        lbcard1.setGeometry(170,55,100,100)
        lbcard1.setStyleSheet("background-color:transparent;")
        lbcard1.setPixmap(QPixmap(r"Frames\icons\deposit_9334619.png").scaled(100,100))
        

        ppu = QLabel(card_view1)
        ppu.setPixmap(QPixmap(r"Frames\icons\ppu.png").scaled(32,32))
        ppu.setGeometry(10,82,32,32)
        ppu.setStyleSheet("background-color:transparent;")
        
        self.view_id_card = QLineEdit(card_view1)
        self.view_id_card.setEnabled(False)
        self.view_id_card.setStyleSheet("font-size:20px;border-radius:0px;background-color:transparent;color:#ffffff;padding-left:12px;font:bold;")
        self.view_id_card.setGeometry(30,160,230,30)
        
        card_view1.setGeometry(10,300,340,200)
        
        
    def on_combobox_change(self):
        # Tables des options pour les différentes sélections
        tab_mad = ["Fès", "Casablanca", "Rabat", "Meknès"]
        tab_cfa = ["Libreville", "Franceville", "Lambarene", "Mouila"]
        # Récupérer la valeur sélectionnée dans le QComboBox
        selected_value = self.balncelft3.currentText()
        # Vider le deuxième QComboBox avant de le remplir
        self.balncelft4.clear()
        # Ajouter les villes correspondantes selon le pays sélectionné
        if selected_value == "Maroc":
            self.balncelft4.addItems(tab_mad)
        elif selected_value == "Gabon":
            self.balncelft4.addItems(tab_cfa)
        
            
        
    def create_security_privilege(self):
        username = self.username_sec.currentText()
        password = self.password_sec.text()
        user_type = self.user_type_sec.currentText()
        activation_code = self.activation_code_sec.text()
        try:
            name, firstname = username.split(" ")
        except:
            return
        id_user = get_id_user(name, firstname)
        
        status = self.actifac.isChecked()
        
        if id_user is not None:
            message = create_security(username, password, user_type, activation_code, id_user, status)
            self.show_message("Privilèges", message if message else "Échec de l'attribution des privilèges")
        else:
            self.show_message("Erreur", "Utilisateur non trouvé")

        # Correction de la méthode getallusers
    def getallusers(self, combo: QComboBox):
        combo.clear()
        users = get_all_users(self.code_user)
        if(len(users)!=0):
            combo.addItems(users)
        else:
            return 
    
    def genered(self):
        self.password_sec.setText(self.generate_unique_password())
        self.generated.setChecked(False)
        
    def generedIDMAD(self):
        data = self.nameuser.currentText()
        if not data or data == "Nom utilisateur":
            self.show_message("Génération ID de la carte", "Veuillez choisir un utilisateur avant de générer l'ID.")
            self.check_id_card2.setChecked(False)
        else:
            try:
                name, firstname = data.split(" ")
                user_id = get_id_user(name, firstname)
                card_code = self.generate_card_number("MAD", user_id)
                self.view_id_card.setText(self.format_with_spaces(card_code, 4))
                self.check_id_card2.setChecked(True)
            except Exception as e:
                self.show_message("Génération ID de la carte", f"Erreur lors de la génération de l'ID : {str(e)}")
                self.check_id_card2.setChecked(False)

    def generedIDFCFA(self):
        data = self.nameuser1.currentText()
        if not data or data == "Nom utilisateur":
            self.show_message("Génération ID de la carte", "Veuillez choisir un utilisateur avant de générer l'ID.")
            self.check_id_card.setChecked(False)
        else:
            try:
                name, firstname = data.split(" ")
                user_id = get_id_user(name, firstname)
                card_code = self.generate_card_number("FCFA", user_id)
                self.view_id_card2.setText(self.format_with_spaces(card_code, 4))
                self.check_id_card.setChecked(True)
            except Exception as e:
                self.show_message("Génération ID de la carte", f"Erreur lors de la génération de l'ID : {str(e)}")
                self.check_id_card.setChecked(False)

    
    def generatednum(self):
        self.activation_code_sec.setText(self.generate_numeric_code())
        self.generated_code.setChecked(False)

    def generate_numeric_code(self,length: int = 8) -> str:
        """Génère un code numérique aléatoire de la longueur spécifiée."""
        code = ''.join(random.choice('0123456789') for _ in range(length))
        return code
        
    def createuser(self):
        """
        Collects user information from input fields, creates a new user, updates the user list, and shows a message.
        """
        # Get text from input fields, remove extra spaces, and assign to variables
        nom = self.balncelft1.text().strip()
        prenom = self.balncelft2.text().strip()
        pays = self.balncelft3.currentText().strip()
        ville = self.balncelft4.currentText().strip()
        cni = self.balncelft5.text().strip()
        phone = self.balncelft6.text().strip()
        email = self.balncelft7.text().strip()

        tab = ["Maroc", "Gabon"]
        
        if(nom=="" or prenom=="" or pays not in tab or phone=="" or  email=="" or cni=="" or ville==""):
            QMessageBox.information(self,"Information","Renseignez toutes les informations sur l'utilisateur avant enregistrement")
            return
        # Call create_user function with gathered data
        retour = create_user(nom, prenom, pays, phone, email, cni, ville)

        # Update user lists (this seems redundant, consider consolidating if possible)
        self.getallusers(self.username_sec)
        self.getallusers(self.nameuser)
        self.getallusers(self.nameuser1)

        # Display a message to the user with the result of the create_user operation
        self.show_message("Création utilisateur", retour)

        # Clear the input fields after user creation
        self.balncelft1.clear()
        self.balncelft2.clear()
        self.balncelft3.clear()
        self.balncelft4.clear()
        self.balncelft5.clear()
        self.balncelft6.clear()
        self.balncelft7.clear()

        
    def createmadaccount(self):
        data = self.nameuser.currentText()
        if data == "Nom utilisateur":
            self.show_message("Création compte MAD", "Opération invalide : Veuillez sélectionner un utilisateur.")
        else:
            try:
                name, firstname = data.split(" ")
                id_user = get_id_user(name, firstname)
                
                code = self.view_id_card.text().replace(" ", "")
                status = self.choix1.isChecked()
                message = create_new_account_mad_request(0, str(code), int(id_user),bool(status))
                self.show_message("Création compte MAD",message)
            except Exception as e:
                self.show_message("Création compte MAD", f"Erreur lors de la création du compte : {str(e)}")

    def createfcfaaccount(self):
        data = self.nameuser1.currentText()
        if data == "Nom utilisateur":
            self.show_message("Création compte FCFA", "Opération invalide : Veuillez sélectionner un utilisateur.")
        else:
            try:
                name, firstname = data.split(" ")
                id_user = get_id_user(name, firstname)
                code = self.view_id_card2.text().replace(" ", "")
                status = self.choix1f.isChecked()
                message = create_new_account_fcfa(0.0, code, id_user, status)
                
                if not message:
                    self.show_message("Création compte FCFA", "Un compte existe déjà pour cet utilisateur.")
                else:
                    self.show_message("Création compte FCFA", "Compte créé avec succès.")
            
            except Exception as e:
                self.show_message("Création compte FCFA", f"Erreur lors de la création du compte : {str(e)}")

        
        
        
    def invoivepanel(self):
        # Sélectionner une option spécifique (assurez-vous que b2 est défini)
        self.selectionOption(self.b2)
        # Création du panel principal et des layouts
        panel_transaction = QWidget()
        layout_transaction = QHBoxLayout(panel_transaction)
        # Définir les listes pour les QComboBox
        transaction_type_liste = ["Nature Transaction", "Envoie", "Retrait"]
        pays_emission_liste = ["Pays Emission", "Maroc", "Gabon"]
        methode_paiement_liste = ["Mode Paiement", "Espece", "Carte"]
        
        winleft = QWidget()
        winleft_layout = QVBoxLayout()
        top_pan = QWidget()
        top_pan_layout = QHBoxLayout()
        top_pan.setStyleSheet("background-color:#3D3D3D;border-radius:12px;")
        one_frame_top = QWidget()
        one_frame_top.setFixedWidth(175)
        one_frame_top.setStyleSheet("background:rgba(75, 255, 179, 89)")
        
        three_frame_top = QWidget()
        three_frame_top.setFixedWidth(175)
        three_frame_top.setStyleSheet("background:rgba(75, 255, 179, 89)")
        
        
        # Créer le QGroupBox pour contenir les boutons radio
        groupRadio = QGroupBox("Choisir la Devise Emettrice",one_frame_top)
        # Créer les QRadioButton pour les options de devises
        dh_choice = QRadioButton("MAD",groupRadio)
        dh_choice.setChecked(True)
        fcfa_choice = QRadioButton("FCFA",groupRadio)
        # Ajouter les QRadioButton au QGroupBox
        dh_choice.setGeometry(12,17,100,20)
        dh_choice.setStyleSheet("background:transparent;font-size:10px;font-weight: bold;color:#ffffff;")
        fcfa_choice.setGeometry(100,17,100,20)
        fcfa_choice.setStyleSheet("background:transparent;font-size:10px;font-weight: bold;color:#ffffff;")
        groupRadio.setFixedHeight(250)
        groupRadio.setStyleSheet("background:transparent;font-weight: bold;color:#ffffff;")
        
        printrecharge = QPushButton("Imprime recharge",one_frame_top)
        printrecharge.clicked.connect(self.print_recharge_card)
        printrecharge.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        printrecharge.setIcon(QIcon(QPixmap(r"Frames\icons\printer_8139457.png")))
        printrecharge.setGeometry(12,220,148,30)
        
        self.userexist = QComboBox(three_frame_top)
        self.userexist.setPlaceholderText("Recepteur")
        self.userexist.setStyleSheet("background-color:#2E2E2E;border-radius:4px;font-weight: bold;color:#ffffff;")
        self.userexist.setGeometry(12,65,148,30)
        self.getallusers(self.userexist)
        
        userexist2 = QLineEdit(three_frame_top)
        userexist2.setPlaceholderText("Recherche Em. par ID")
        userexist2.setStyleSheet("border-radius:4px;padding-left:12px;font-weight: bold;color:#ffffff;")
        userexist2.setGeometry(12,100,148,30)
        
            
        searcheuser_by_id = QLineEdit(three_frame_top)
        searcheuser_by_id.setGeometry(12,30,148,30)
        searcheuser_by_id.setPlaceholderText("Recherche Re. par ID")
        searcheuser_by_id.setStyleSheet("border-radius:4px;font:bold;padding-left;")
        
        self.userexist3 = QComboBox(three_frame_top)
        self.userexist3.setPlaceholderText("Emetteur")
        self.userexist3.setStyleSheet("background-color:#2E2E2E;border-radius:4px;font-weight: bold;color:#ffffff;")
        self.userexist3.setGeometry(12,135,148,30)
        self.getallusers(self.userexist3)
        
        searcheuser_by_id.textChanged.connect(self.search_clientB)
        userexist2.textChanged.connect(self.search_clientC)
        
        # Créer le QGroupBox pour contenir les boutons radio
        groupRadio2 = QGroupBox("Status Frais Transaction/AM",three_frame_top)
        # Créer les QRadioButton pour les options de devises
        applique_choice = QRadioButton("Avec Frais",groupRadio2)
        noapplique_choice = QRadioButton("Sans Frais",groupRadio2)
        applique_choice.setStyleSheet("background:transparent;font-size:10px;font-weight: bold;color:#ffffff;")
        noapplique_choice.setStyleSheet("background:transparent;font-size:10px;font-weight: bold;color:#ffffff;")
        # Ajouter les QRadioButton au QGroupBox
        applique_choice.setChecked(True)
        applique_choice.setGeometry(5,17,100,20)
        noapplique_choice.setGeometry(95,17,100,20)
        groupRadio2.setFixedHeight(250)
        groupRadio2.setStyleSheet("background:transparent;font-weight: bold;color:#ffffff;")
        
        printFACTURE = QPushButton("Imprime Facture",three_frame_top)
        printFACTURE.clicked.connect(self.print_facture)
        printFACTURE.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        printFACTURE.setIcon(QIcon(QPixmap(r"Frames\icons\printer_8139457.png")))
        printFACTURE.setGeometry(12,220,148,30)
        
        transaction_type = QComboBox(one_frame_top)
        transaction_type.setFixedHeight(30)
        transaction_type.setStyleSheet("background-color:#2E2E2E;border-radius:4px;font-weight: bold;color:#ffffff;")
        pays_emission = QComboBox(one_frame_top)
        pays_emission.setFixedHeight(30) 
        pays_emission.setStyleSheet("background-color:#2E2E2E;border-radius:4px;font-weight: bold;color:#ffffff;")
        methode_paiement = QComboBox(one_frame_top)
        methode_paiement.setFixedHeight(30)
        methode_paiement.setStyleSheet("background-color:#2E2E2E;border-radius:4px;font-weight: bold;color:#ffffff;")
        BP = QLabel(f"BP: {code_BP}",one_frame_top)
        BP.setStyleSheet("background:transparent;font-weight: bold;color:#ffffff;")
        AG = QLabel(f"Agence: {AGENT}",one_frame_top)
        AG.setStyleSheet("background:transparent;font-weight: bold;color:#ffffff;")
        
        transaction_type.addItems(transaction_type_liste)
        pays_emission.addItems(pays_emission_liste)
        methode_paiement.addItems(methode_paiement_liste )
        
        BP.setGeometry(12,5,100,30)
        AG.setGeometry(12,35,120,30)
        groupRadio.setGeometry(5,175,175,30)
        groupRadio2.setGeometry(5,175,175,30)
        transaction_type.setGeometry(12,65,148,30)
        pays_emission.setGeometry(12,100,148,30)
        methode_paiement.setGeometry(12,135,148,30)
        
        
        
        two_frame_top = QWidget()
        two_frame_top_layout = QVBoxLayout()
        
        client_emetteur = QLabel("Emetteur Transaction")
        client_emetteur.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.emetteur = QLineEdit()
        self.emetteur.setPlaceholderText("indicatif/telephone/nom emetteur")
        self.emetteur.setFixedHeight(30)
        self.emetteur.setStyleSheet("background-color:#2E2E2E;padding-left:12px;border-radius:4px;")
        client_recepteur = QLabel("Recepteur Transaction")
        client_recepteur.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.recepteur =  QLineEdit()
        self.recepteur.setPlaceholderText("indicatif/telephone/nom recepteur")
        self.recepteur.setFixedHeight(30)
        self.recepteur.setStyleSheet("background-color:#2E2E2E;padding-left:12px;border-radius:4px;")
        client_solde = QLabel("Solde Transaction")
        client_solde.setStyleSheet("font-weight: bold;color:#ffffff;")
        self.solde =  QLineEdit()
        self.solde.setPlaceholderText("Montant de transaction")
        self.solde.setFixedHeight(30)
        self.solde.setStyleSheet("background-color:#2E2E2E;padding-left:12px;border-radius:4px;")
        
        code_Agent = QLabel(f"{AG_AM}")
        code_Agent.setStyleSheet("margin-left:50px;font-size:24px;")
        
        valide_transaction = QPushButton("Generer Facture")
        valide_transaction.setIcon(QIcon(QPixmap(r"Frames\icons\calculator_7133722.png")))
        valide_transaction.setFixedHeight(30)
        valide_transaction.clicked.connect(self.clicked_genereted_facture)
        valide_transaction.setStyleSheet("""
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        
        
        two_frame_top_layout.addWidget(client_emetteur)
        two_frame_top_layout.addWidget(self.emetteur)
        two_frame_top_layout.addWidget(client_recepteur)
        two_frame_top_layout.addWidget(self.recepteur)
        two_frame_top_layout.addWidget(client_solde)
        two_frame_top_layout.addWidget(self.solde)
        two_frame_top_layout.addWidget(code_Agent)
        two_frame_top_layout.addWidget(valide_transaction)
        two_frame_top.setLayout(two_frame_top_layout)
        
        
        top_pan_layout.addWidget(one_frame_top)
        top_pan_layout.addWidget(two_frame_top)
        top_pan_layout.addWidget(three_frame_top)
        top_pan.setLayout(top_pan_layout)
         
        
        bottom_pan = QWidget()
        vi_ic=QLabel(bottom_pan)
        vi_ic.setGeometry(10,10,50,50)
        vi_ic.setPixmap(QPixmap(r"c:\Users\farya\Downloads\money-transfer_9815918.png").scaled(50,50))
        bottom_pan.setStyleSheet("background-color:#3D3D3D;border-radius:12px;")
        
        grt = QGroupBox("Choix de transaction:",bottom_pan)
        grt.setStyleSheet("font-weight: bold;color:#ffffff;")
        ch1 = QRadioButton("Instantanée",grt)
        ch1.setChecked(True)
        ch2 = QRadioButton("Client existant",grt)
        ch3 = QRadioButton("Recharge compte",grt)
        ch4 = QRadioButton("Generer carte",grt)
        ch1.setGeometry(10,15,148,30)
        ch2.setGeometry(120,15,148,30)
        ch3.setGeometry(230,15,148,30)
        ch4.setGeometry(360,15,148,30)
        grt.setGeometry(100,10,500,50) 
        
        wid_recharge = QWidget(bottom_pan)
        
        wid_recharge.setStyleSheet("background-color:#2E2E2E;padding-left:12px;border-radius:4px;")
        wid_recharge.setGeometry(10,80,290,170) 
        
        lb_ss= QLabel("Identifiant de la carte:",wid_recharge)
        lb_ss.setStyleSheet("color:#ffffff;font-weight: bold;")
        lb_ss.setGeometry(0,8,200,10)
        
        self.sold = QLineEdit(wid_recharge)
        self.sold.setPlaceholderText("Recherche bénéficiaire par ID")
        self.sold.setStyleSheet("background-color:#ffffff;font-weight: bold;color:black;")
        self.sold.setGeometry(10,30,270,30)
        
        lb_sr= QLabel("Nom du client:",wid_recharge)
        lb_sr.setStyleSheet("color: #ffffff;font-weight: bold;")
        lb_sr.setGeometry(0,70,200,10)
        
        self.client_recep = QComboBox(wid_recharge)
        self.client_recep.setPlaceholderText("Nom du bénéficiaire de la recharge")
        self.client_recep.setStyleSheet("background-color:#3D3D3D;font-weight: bold;")
        self.client_recep.setGeometry(10,90,270,30)
        self.getallusers(self.client_recep)
        self.sold.textChanged.connect(self.search_clientA)
        
        self.montlab = QLabel("Montant:",wid_recharge)
        self.montlab.setStyleSheet("color: #ffffff;font-weight: bold;")
        self.montlab.setGeometry(130, 135, 90, 30)
    
        self.mont = QLineEdit(wid_recharge)
        self.mont.setStyleSheet("background-color: #ffffff; border-radius: 4px; color: black; font-weight: bold;")
        self.mont.setGeometry(200, 135, 80, 30)
        
        gen_card = QPushButton("generer recharge",wid_recharge)
        gen_card.clicked.connect(self.generate_recharge)
        gen_card.setIcon(QIcon(QPixmap(r"Frames\icons\credit-card_6296460.png")))
        gen_card.setGeometry(10,135,130,30)
        gen_card.setStyleSheet(
                               """
                          QPushButton{background-color:#4BFFB3;color:black;border-radius:4px;font:bold;}
        
                QPushButton:pressed 
            {
                background-color: #00ee63;
                border-style: inset;
            }
            """)
        

        
        wid_recharge2 = QWidget(bottom_pan)
        self.view_card_recharge = QTextEdit(wid_recharge2)
        self.view_card_recharge.setReadOnly(True)
        self.info_fact = """
                Carte de Recharge AryadMoney      
        ---------------------------------------------
        Code recharge: {code_recharge}        
                                                {montant} {devise}      
        ---------------------------------------------
        Contactez-Nous:                       
        Adresse de contact: {adresse}        
        Téléphone de contact: {PHONE} 
        """
        self.update_recharge()       
        self.view_card_recharge.setGeometry(0,0,290,170)
        self.view_card_recharge.setStyleSheet("background-color:#ffffff;border-radius:4px;color:black;")
        wid_recharge2.setStyleSheet("background-color:#2E2E2E;padding-left:12px;border-radius:4px;")
        wid_recharge2.setGeometry(305,80,290,170)  
        
        winleft_layout.addWidget(top_pan)
        winleft_layout.addWidget(bottom_pan)
        winleft.setLayout(winleft_layout)
        
        
        
        winright = QWidget()
        self.facture_view = QTextEdit(winright)
        self.info_facture = """
                            Résumé de transaction
        --------------------------------------------------
                                    AryadMoney
            
        Facture N°: {numero_facture}
        Date: {date}
        --------------------------------------------------
        Emetteur:
        Nom du client: {emetteur_nom}
        Adresse du client: {emetteur_adresse}
        Email du client: {emetteur_recepteur}
        Téléphone du client: {telephone_emetteur}
        --------------------------------------------------
        Sous-Total: {argent}
        Frais de Service: {frais_argent}
        Total à Payer: {total_argent}
        --------------------------------------------------
                     Merci pour votre confiance !
        --------------------------------------------------
                                 Net à recevoir
                                        {net_recu}
        --------------------------------------------------
        Recepteur:
        Nom du client: {client_nom}
        Adresse du client: {client_adresse}
        Email du client: {client_email}
        Téléphone du client: {client_recepteur}
        --------------------------------------------------
        Contactez-Nous:
        Adresse de contact: {ADDC}
        Téléphone de contact: {PHONE}
        Email de contact: {EMAIL}
"""
        
        self.facture_view.setText(self.info_facture)
        self.update_facture()
        self.facture_view.setReadOnly(True)
        self.facture_view.setStyleSheet("background-color:white;color:black;")
        self.facture_view.setGeometry(0,0,300,564)
        winright.setFixedWidth(300)
        winright.setStyleSheet("background-color:#3D3D3D;border-radius:12px;")
        
        layout_transaction.addWidget(winleft)
        layout_transaction.addWidget(winright)
        # Définir le layout principal pour le panel
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color:#2E2E2E;")
        # Remplacer l'ancien widget par le nouveau panel_transaction
        self.replace_widget(self.old_wid, panel_transaction)
    
    def generate_recharge(self):
        self.montn = self.mont.text().replace(" ", "")
        recharge = self.client_recep.currentText()
        self.code=self.generate_unique_recharge_code()
        name,firstname = recharge.split(" ")
        info = devise_client_account(name,firstname)
        devise = info["devise"]
        card = info["card"]
        
        self.sold.setText(card)
        
        if self.montn.isdigit() and recharge and float(self.montn)>0 and devise is not None:
            self.update_recharge(mont_=self.montn,code_recharge_=self.code,devise_=devise)
        else:
            self.mont.setText("")
            QMessageBox.warning(self, "Operation Invalid", "montant ou beneficiaire invalid")

    def search_clientA(self,value):
        if len(value) == 16:
            response = info_client(value)  # Ajout de self pour appeler la méthode de la classe
            if response is None:
                message = "Client non existant"
                QMessageBox.warning(self, "Opération invalide",message)
                self.client_recep.setCurrentText(message)
            else:
                name_user=response["name_user"]
                self.client_recep.setCurrentText(name_user)
                self.update_recharge(devise_=response["devise"])

    
    def search_clientC(self,value):
        if len(value) == 16:
            response = info_client(value)  # Ajout de self pour appeler la méthode de la classe
            if response is None:
                message = "Client non existant"
                QMessageBox.warning(self, "Opération invalide",message)
                self.userexist3.setCurrentText(message)
            else:
                name_user=response["name_user"]
                self.userexist3.setCurrentText(name_user)
                self.update_recharge(devise_=response["devise"])
        
    def search_clientB(self,value):
        if len(value) == 16:
            response = info_client(value)  # Ajout de self pour appeler la méthode de la classe
            if response is None:
                message = "Client non existant"
                QMessageBox.warning(self, "Opération invalide",message)
                self.userexist.setCurrentText(message)
            else:
                name_user=response["name_user"]
                self.userexist.setCurrentText(name_user)
                self.update_recharge(devise_=response["devise"])
    
    def update_recharge(self,
                mont_="XXXX",
                code_recharge_="XXXXXXXXXXXX", 
                devise_="MAD",
                adresse_=ADDC,        
                PHONE_=PHONE):
        info_fact = self.info_fact.format(
                code_recharge=code_recharge_,        
                montant=mont_,
                devise=devise_,
                adresse=adresse_,        
                PHONE=PHONE_)
        self.view_card_recharge.setText(info_fact)
    
    def generate_unique_recharge_code(self, length=16):
        digits = string.digits
        recharge_code = ''.join(random.choice(digits) for _ in range(length))
        return recharge_code
    
    def ensure_directory_exists(self,file_path):
        # Crée le répertoire s'il n'existe pas
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def print_recharge_card(self):
        montn = self.mont.text().replace(" ", "")
        recharge = self.client_recep.currentText()
        name,firstname = recharge.split(" ")
        info = devise_client_account(name,firstname)
        message = create_recharge_card(info["user_id"],self.code,montn,info["card"])
        # Crée un objet QPrinter configuré pour exporter en PDF
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        date_imp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")  # Format de date plus sûr pour les fichiers
        pdf_name = f"recharge_{date_imp}.pdf"
        # Définissez le chemin où le fichier PDF sera enregistré
        pdf_path = os.path.join("recharges", f"Aryad_{pdf_name}")
        # Assurez-vous que le répertoire existe
        self.ensure_directory_exists(pdf_path)
        printer.setOutputFileName(pdf_path)
        # Imprime le contenu du QTextEdit dans le fichier PDF
        self.view_card_recharge.print_(printer)
        QMessageBox.information(self, "Information", f"Recharge generée avec succès")
        # Ouvre le fichier PDF dans le navigateur par défaut
        webbrowser.open_new(pdf_path)
    def print_facture(self):
        # Crée un objet QPrinter configuré pour exporter en PDF
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        date_imp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")  # Format de date plus sûr pour les fichiers
        pdf_name = f"facture_{date_imp}.pdf"
        # Définissez le chemin où le fichier PDF sera enregistré
        pdf_path = os.path.join("factures", f"Aryad_{pdf_name}")
        # Assurez-vous que le répertoire existe
        self.ensure_directory_exists(pdf_path)
        printer.setOutputFileName(pdf_path)
        # Imprime le contenu du QTextEdit dans le fichier PDF
        self.facture_view.print_(printer)
        QMessageBox.information(self, "Information", f"Facture generée avec succès")
        # Ouvre le fichier PDF dans le navigateur par défaut
        webbrowser.open_new(pdf_path)


    def replace_widget(self,old_wid,new_wid):
        self.old_wid = new_wid
        index = self.layout.indexOf(old_wid)
        if index != -1:
            # Remove the old widget
            old_widget = self.layout.itemAt(index).widget()
            self.layout.removeWidget(old_widget)
            old_widget.setParent(None)  # This line is important to delete the old widget

            # Add the new widget at the same position
            self.layout.insertWidget(index,new_wid)
    
    def selectionOption(self,win):
        self.selected.setStyleSheet("background-color:transparent;")
        win.setStyleSheet("background-color:#4BFFB3;")
        self.selected = win
        
    def declaration(self,code):
        self.titlecomp = QLabel("AryadMoney")
        self.titlecomp.setStyleSheet("font-weight: bold;font-size:18px;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        
        self.topcentralpan()
        self.centrepan(code)
       
    def topcentralpan(self):
        self.sous_panel_central_top = QWidget()
        self.sous_panel_central_top.setFixedHeight(60)

        w1 = QWidget()
        lay_out = QHBoxLayout()
        btn_search = QPushButton()
        barre_search = QLineEdit()
        barre_search.setPlaceholderText("Search")
        barre_search.setStyleSheet("color:black;")
        btn_search.setIcon(QIcon(QPixmap(r"Frames\icons\icon5.png")))
        lay_out.addWidget(barre_search)
        lay_out.addWidget(btn_search)
        w1.setStyleSheet("background-color:#D9D9D9;border-radius:10px;")
        w1.setFixedSize(300,40)
        w1.setLayout(lay_out)

        w2 = QWidget()
        w2_layout = QHBoxLayout()
        w2.setFixedSize(100,40)
        b1 = QPushButton("")
        b1.setIcon(QIcon(QPixmap(r"Frames\icons\icon1.png")))
        b1.setStyleSheet("background-color:transparent;")
        b1.setFixedSize(36,36)
        b2 = QPushButton("")
        b2.setIcon(QIcon(QPixmap(r"Frames\icons\18.png")))
        b2.setStyleSheet("background-color:transparent;")
        b2.setFixedSize(36,36)
        b3 = QPushButton("")
        b3.setIcon(QIcon(QPixmap(r"Frames\icons\icon3.png")))
        b3.setStyleSheet("background-color:transparent;")
        b3.setFixedSize(36,36)
        b4 = QPushButton("")
        b4.setIcon(QIcon(QPixmap(r"Frames\icons\icon4.png")))
        b4.setStyleSheet("background-color:transparent;")
        b4.setFixedSize(36,36)
        b3.setFixedSize(36,36)
        w2_layout.addWidget(b1)
        w2_layout.addWidget(b2)
        w2_layout.addWidget(b3)
        w2_layout.addWidget(b4)
        w2.setLayout(w2_layout)
        w2.setStyleSheet("margin-bottom:12px;")

        w3 = QWidget()
        lay_out2 = QHBoxLayout()
        text_lab = QLabel("Generer Raport")
        text_lab.setStyleSheet("color: #ffffff;font-weight: bold;")
        lab_icon = QLabel()
        lab_icon.setPixmap(QPixmap(r"Frames\icons\icon6.png").scaled(16,16))
        lay_out2.addWidget(text_lab)
        lay_out2.addWidget(lab_icon)
        w3.setFixedSize(130,40)
        w3.setStyleSheet("background-color:#5B24E0;border-radius:10px;")
        w3.setLayout(lay_out2)
        
        top_lauout =QHBoxLayout()
        top_lauout.addWidget(self.titlecomp) 
        top_lauout.addWidget(w1)
        top_lauout.addWidget(w2)
        top_lauout.addWidget(w3)
        self.sous_panel_central_top.setLayout(top_lauout)
        self.sous_panel_central_top.setStyleSheet("background-color:#2E2E2E;")
    
    def centrepan(self,code):
        self.code_user = code
        self.sous_panel_central_central = QWidget()
        self.sous_panel_central_central.setStyleSheet("background-color:#2E2E2E")
        sous_panel_central_central_layout = QHBoxLayout()

        sous_panel_central_central_sous1 = QWidget()
        sous_panel_central_central_sous1.setFixedWidth(700)
        slayout = QVBoxLayout()
        
        s1 =QWidget()
        card = QWidget(s1)
        card.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1,  stop: 0 #284AA5, stop: 1 #4B7DFF);")

        card2 = QWidget(s1)
        card2.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1, stop:0#4BFF93,stop:1#32A528);")

        l1 = QLabel("Current Balance",card)
        info_cdh = get_balance_mad(code)
        l2 = QLabel(f"{self.format_with_spaces(info_cdh["id_card"],4)}",card)
        l3 = QLabel(f"MAD {info_cdh["balance"]}",card)
        l4 = QLabel("09/25",card)
        l5 = QLabel("Aryad",card)
        
        

        puce1 = QLabel(card)
        puce1.setPixmap(QPixmap(r"Frames\icons\puce.png").scaled(47,37))
        puce1.setGeometry(45,80,47,37)

        puce2 = QLabel(card2)
        puce2.setPixmap(QPixmap(r"Frames\icons\puce.png").scaled(47,37))
        puce2.setGeometry(45,80,47,37)

        ppu = QLabel(card)
        ppu.setPixmap(QPixmap(r"Frames\icons\ppu.png").scaled(32,32))
        ppu.setGeometry(10,82,32,32)
        ppu.setStyleSheet("background-color:transparent;")

        ppu2 = QLabel(card2)
        ppu2.setPixmap(QPixmap(r"Frames\icons\ppu.png").scaled(32,32))
        ppu2.setGeometry(10,82,32,32)
        ppu2.setStyleSheet("background-color:transparent;")

        l1_1 = QLabel("Current Balance",card2)
        info_cfcfa = get_balance_fcfa(code)
        l2_2 = QLabel(self.format_with_spaces(info_cfcfa["id_card"],4),card2)
        l3_3 = QLabel(f"FCFA {self.format_with_spaces(info_cfcfa["balance"],3)}",card2)
        l4_4 = QLabel("09/25",card2)
        l5_5 = QLabel("Aryad",card2)

        l1.setGeometry(15,10,200,30)
        l1.setStyleSheet("font-size:15px;background:transparent;")

        l2.setGeometry(15,140,200,30)
        l2.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        l3.setGeometry(15,32,200,30)
        l3.setStyleSheet("font-size:20px;font:bold;background:transparent;")

        logo = QLabel(card)
        logo.setStyleSheet("background:transparent;")
        logo.setPixmap(QPixmap(r"Frames\icons\13.png").scaled(43,27))
        logo.setGeometry(240,10,50,60)

        l4.setGeometry(235,140,40,20)
        l4.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        l5.setGeometry(251,50,50,15)
        l5.setStyleSheet("background:transparent;font-size:8px;")


        l1_1.setGeometry(15,10,200,30)
        l1_1.setStyleSheet("font-size:15px;background:transparent;")

        l2_2.setGeometry(15,140,200,30)
        l2_2.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        l3_3.setGeometry(15,32,200,30)
        l3_3.setStyleSheet("font-size:20px;font:bold;background:transparent;")

        logo_2 = QLabel(card2)
        logo_2.setStyleSheet("background:transparent;")
        logo_2.setPixmap(QPixmap(r"Frames\icons\13.png").scaled(43,27))
        logo_2.setGeometry(240,10,50,60)

        l4_4.setGeometry(235,140,40,20)
        l4_4.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        l5_5.setGeometry(251,50,50,15)
        l5_5.setStyleSheet("background:transparent;font-size:8px;")
        card.setGeometry(10,13,300,178)
        card2.setGeometry(370,13,300,178)
        s1.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")

        self.defilementHistorique()

        historique_label = QLabel("Historique des paiements",self.s2)
        historique_label.setGeometry(10,10,300,25)
        historique_label.setStyleSheet("font-size:18px;font:bold;color:#4BFFB3;font-weight: bold;")

        slayout.addWidget(s1)
        slayout.addWidget(self.s2)
        sous_panel_central_central_sous1.setLayout(slayout)
        sous_panel_central_central_sous1.setStyleSheet("background-color:#2E2E2E")

        sous_panel_central_central_sous2 = QWidget()
        sous_panel_central_central_sous2.setFixedWidth(200)
        slayout2 = QVBoxLayout()
        s12 =QWidget()

        s1_pan_in = QWidget(s12)
        s1_pan_in.setStyleSheet("background-color:rgba(75, 255, 179, 89);border-radius:15px;")
        s1_pan_in.setGeometry(10,110,160,85)

        factures = QLabel(s1_pan_in)
        factures.setStyleSheet("background-color:transparent;")
        factures.setPixmap(QPixmap(r"Frames\icons\factures.png").scaled(45,55))
        factures.setGeometry(20,10,45,55)

        btn_facture = QPushButton("Factures",s1_pan_in)
        btn_facture.setGeometry(17,60,50,20)
        btn_facture.setStyleSheet("font-size:10px;font:bold;color:black;background-color:transparent;")


        Commission = QLabel(s1_pan_in)
        Commission.setStyleSheet("background-color:transparent;")
        Commission.setPixmap(QPixmap(r"Frames\icons\com.png").scaled(45,55))
        Commission.setGeometry(90,10,45,55)

        btn_commission = QPushButton("Commissions",s1_pan_in)
        btn_commission.setGeometry(82,60,61,20)
        btn_commission.setStyleSheet("font-size:10px;font:bold;color:black;background-color:transparent;")

        s12.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")

        s22 = QWidget()
        label_rescent = QLabel("Transactions rescentes",s22)
        label_rescent.setStyleSheet("font-size:15px;font:bold;color:#4BFFB3;font-weight: bold;")
        label_rescent.setGeometry(10,10,160,20)

        self.frame_scroll = QScrollArea(s22)
        self.deviseA, self.deviseB = "MAD", "FCFA"
        self.gethistorescente(self.frame_scroll)
        self.frame_scroll.setGeometry(0,30,181,200)
        self.frame_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frame_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frame_scroll.setWidgetResizable(True)
        
        s22.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")
        slayout2.addWidget(s12)
        slayout2.addWidget(s22)
        sous_panel_central_central_sous2.setLayout(slayout2)
        sous_panel_central_central_sous2.setStyleSheet("background-color:#2E2E2E")
        sous_panel_central_central_layout.addWidget(sous_panel_central_central_sous1)
        sous_panel_central_central_layout.addWidget(sous_panel_central_central_sous2)
        self.sous_panel_central_central.setLayout(sous_panel_central_central_layout)

    def gethistorescente(self,b):
        Historiques = get_all_history(self.code_user)
        if Historiques is not None:
            frame_rescent = QWidget()
            frame_layout = QVBoxLayout()
            for elmt in Historiques:
                # Convertir en objet datetime
                datetime_obj = elmt["transaction_date"][:10].replace("T"," ")
                day = str(datetime.now())[:10].replace("T"," ")
                if datetime_obj == day:
                    t = QWidget()
                    t_layout = QHBoxLayout()
                    i = QLabel()
                    i.setStyleSheet("background:#2E2E2E;border-radius:15px;")
                    i.setAlignment(Qt.AlignCenter)
                    i.setFixedSize(32, 32)

                    j = QLabel()
                    k = QLabel()

                    if elmt["transaction_type"] == "envoie":
                        i.setPixmap(QPixmap(r"Frames\icons\190.png").scaled(20, 20))
                        j.setText("Envoie")
                        k.setText(f"+{self.deviseA} {elmt['transaction_amount']}")
                    elif elmt["transaction_type"] == "retrait":
                        i.setPixmap(QPixmap(r"Frames\icons\17.png").scaled(20, 20))
                        j.setText("Retrait")
                        k.setText(f"-{self.deviseB} {elmt['transaction_amount']}")

                    t_layout.addWidget(i)
                    t_layout.addWidget(j)
                    t_layout.addWidget(k)
                    t.setLayout(t_layout)
                    t.setFixedSize(160, 50)
                    frame_layout.addWidget(t)
            frame_rescent.setLayout(frame_layout)
            b.setWidget(frame_rescent)
    
    def clear_layout(self,layout):
        while layout.count():
            item = layout.takeAt(0)  # Prend l'élément du layout
            widget = item.widget()  # Récupère le widget de l'élément (si c'est un widget)
            if widget:
                widget.deleteLater()  # Supprime le widget


    def defilementHistorique(self):
        self.s2 = QWidget()
        self.s2.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")
        scroll = QScrollArea(self.s2)
        slide_historique = QWidget()
        
        slide_historique_layout =  self.refresh()
        slide_historique.setLayout(slide_historique_layout)
        #Scroll Area Properties
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(slide_historique)
        scroll.setGeometry(10,40,660,180)
        
        
    def refresh(self):
        slide_historique_layout = QVBoxLayout()
        self.clear_layout(slide_historique_layout)
        Historiques = get_all_history(self.code_user)
        if Historiques is not None:  # Vérifier si la liste des historiques n'est pas vide
            for histo in Historiques:
                h1 = QWidget()
                icon = QLabel("")
                icon.setAlignment(Qt.AlignCenter)
                icon.setFixedSize(32,32)
                icon.setStyleSheet("background:#2E2E2E;border-radius:15px;border:transparent;")
                if histo["transaction_type"] == "envoie":
                    icon.setPixmap(QPixmap(r"Frames\icons\190.png").scaled(20,20))
                   
                if histo["transaction_type"] == "retrait":
                    icon.setPixmap(QPixmap(r"Frames\icons\17.png").scaled(20,20))
                   
                # Assurez-vous que les clés existent et que les données sont correctement formatées
                recever = QLabel(str(histo.get("receiver","Inconnu")))
                recever.setStyleSheet("background-color:transparent;border:transparent;")
                sender = QLabel(str(histo.get("sender", "Inconnu")))
                sender.setStyleSheet("background-color:transparent;border:transparent;")
                date = QLabel(str(histo.get("transaction_date", "Date inconnue"))[:19].replace("T"," "))
                date.setStyleSheet("background-color:transparent;border:transparent;")
                argent = QLabel(str(histo.get("transaction_amount", "0.0")))
                argent.setStyleSheet("background-color:transparent;border:transparent;")
                free = QLabel(str(histo.get("transaction_fee","0.0")))
                free.setStyleSheet("background-color:transparent;border:transparent;")
                nature = QLabel(histo.get("transaction_type", "Nature inconnue"))
                nature.setStyleSheet("background-color:transparent;border:transparent;")
            
                
                layout_pan_histo = QHBoxLayout()
                layout_pan_histo.addWidget(icon)

                layout_pan_histo.addWidget(recever)
                layout_pan_histo.addWidget(sender)
                layout_pan_histo.addWidget(date)
                layout_pan_histo.addWidget(argent)
                layout_pan_histo.addWidget(free)
                layout_pan_histo.addWidget(nature)

                h1.setStyleSheet("background-color:black;border-bottom:1px solid blue;border-radius:0px")
                h1.setFixedHeight(50)
                h1.setLayout(layout_pan_histo)
                slide_historique_layout.addWidget(h1)
                
        return  slide_historique_layout
        
        
    
    def format_with_spaces(self,number,c):
        # Convertir le nombre en chaîne de caractères s'il ne l'est pas déjà
        number_str = str(number)
        # Découper la chaîne en morceaux de 4 caractères
        chunks = [number_str[i:i+c] for i in range(0, len(number_str), c)]
        # Joindre les morceaux avec un espace
        formatted_number = ' '.join(chunks)
        return formatted_number
    
    def update_facture(self,numero_facture_="",
            date_="",
            emetteur_nom_="",
            emetteur_adresse_="",
            emetteur_recepteur_="",
            telephone_emetteur_="",
            argent_="",
            frais_argent_="",
            total_argent_="",
            net_recu_ = "",
            client_nom_ = "",
            client_adresse_ = "",
            client_email_ = "",
            client_recepteur_ = "",
            ADDC_=ADDC,
            PHONE_=PHONE,
            EMAIL_=EMAIL):
        # Replace placeholders with actual data
        info_facture_filled = self.info_facture.format(
            numero_facture=numero_facture_,
            date=date_,
            emetteur_nom=emetteur_nom_,
            emetteur_adresse=emetteur_adresse_,
            emetteur_recepteur=emetteur_recepteur_,
            telephone_emetteur=telephone_emetteur_,
            argent=argent_,
            frais_argent=frais_argent_,
            total_argent=total_argent_,
            net_recu = net_recu_,
            client_nom = client_nom_,
            client_adresse = client_adresse_,
            client_email = client_email_,
            client_recepteur = client_recepteur_,
            ADDC= ADDC_,
            PHONE= PHONE_,
            EMAIL= EMAIL_)
        self.facture_view.setText(info_facture_filled)
    
    

    def is_valid_phone_number(self,phone_number):
        # Définir le motif pour un numéro de téléphone international ou national
        pattern = r"^\+?\d{1,3}[- ]?\d{1,4}[- ]?\d{3,4}[- ]?\d{4}$"
        # Utiliser re.match pour vérifier si la chaîne correspond au motif
        return re.match(pattern, phone_number) is not None
            
    def clicked_genereted_facture(self):
        
        if self.emetteur.text().strip() != "" and self.recepteur.text().strip()!="" and self.solde.text().strip()!="":
            # Vérification et séparation pour l'émetteur
            if self.emetteur.text().count("/") != 2 or self.recepteur.text().count("/") != 2:
                if self.recepteur.text().count("/") != 2:
                    self.show_message("Error","Informations du récepteur invalid\n format: (indicatif/numero/nom complet)")
                if self.emetteur.text().count("/") != 2:
                    self.show_message("Error","Informations de l'émetteur invalid\n format: (indicatif/numero/nom complet)")
                else:
                    self.show_message("Echec","Remplissez correctement les champs")
            else:
                indiceE, phone_numberE, nameE = self.emetteur.text().split('/')
                indiceR, phone_numberR, nameR = self.recepteur.text().split('/')
                
                indices = ["+241","+212"]
                

                if indiceE!="" and phone_numberE!="" and nameE!="" and  indiceR!="" and phone_numberR!="" and nameR!="":
                    if (indiceR not in indices or self.is_valid_phone_number(phone_numberR)!=True) or (indiceE not in indices or self.is_valid_phone_number(phone_numberE)!=True):
                        if indiceR not in indices or self.is_valid_phone_number(phone_numberR)!=True :
                            if indiceR not in indices:
                                self.show_message("Error","indicatif recepteur incorect ")
                            elif self.is_valid_phone_number(phone_numberR)!=True:
                                self.show_message("Error","Numero recepteur invalid ")
                            else:
                                self.show_message("Error","informations recepteur invalid ")
                        elif indiceE not in indices or self.is_valid_phone_number(phone_numberE)!=True:
                            if indiceE not in indices:
                                self.show_message("Error","indicatif emetteur incorect ")
                            elif self.is_valid_phone_number(phone_numberE)!=True:
                                self.show_message("Error","Numero emetteur invalid ")
                            else:
                                self.show_message("Error","informations emetteur invalid ")
                        elif indiceR not in indices and indiceE not in indices:
                            self.show_message("Error","indicatifs incorects ")         
                    else:
                        # Suppression des espaces inutiles autour des éléments
                        phone_numberE = f"{indiceE.strip()} {phone_numberE.strip()}"
                        nameE = nameE.strip()
                        phone_numberR = f"{indiceR.strip()} {phone_numberR.strip()}"
                        nameR = nameR.strip()
                        devise = "MAD" if indiceE.strip()=="+212" else "FCFA"
                        solde = self.solde.text().strip()
                        numero_facture=""
                        date= str(datetime.now())
                        emetteur_nom= nameE
                        emetteur_adresse=""
                        emetteur_recepteur=""
                        telephone_emetteur=phone_numberE
                        argent= solde+" "+devise
                        frais_argent= str(round(float(solde)*0.1))+" "+devise
                        total_argent=str(round((float(solde)+round(float(solde)*0.1))))+" "+devise
                        net_recu = str(round(float(solde)*60))+" "+"FCFA" if devise=="MAD" else str(round(float(solde)/60))+" "+"MAD"
                        client_nom = nameR
                        client_adresse = ""
                        client_email = ""
                        client_recepteur = phone_numberR
                        
                        self.update_facture(date_=date,total_argent_=total_argent,frais_argent_=frais_argent,emetteur_nom_=emetteur_nom,telephone_emetteur_=telephone_emetteur,
                                        argent_=argent,client_nom_=client_nom,client_recepteur_=client_recepteur,net_recu_=net_recu)
                else:
                    self.show_message("Echec","Remplissez correctement les champs suivant le format")
        else:
            self.show_message("Echec","Remplissez tous les champs")
        
    def show_message(self,titre,message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(titre)
        msgBox.setStyleSheet("background-color:#5B4040;color:#FF6B4B;")
        msgBox.setText(message)
        msgBox.exec()
    
    

    def generate_unique_password(self,length: int =8) -> str:
        """Génère un mot de passe unique et sécurisé avec une longueur spécifiée."""
        # Combinaison des caractères possibles
        characters = string.ascii_letters + string.digits + string.punctuation
        # Générer un mot de passe aléatoire sécurisé
        password = ''.join(secrets.choice(characters) for i in range(length))
        return password
    
    def generate_card_number(self,currency: str, client_id: int) -> str:
        if currency == "FCFA":
            prefix = "241"
        elif currency == "MAD":
            prefix = "212"
        else:
            raise ValueError("Devise non supportée. Utilisez 'FCFA' ou 'MAD'.")
        # Convertir l'ID du client en chaîne de caractères
        client_id_str = str(client_id)
        # Calculer le nombre de chiffres aléatoires nécessaires pour compléter les 16 chiffres
        num_random_digits = 16 - len(prefix) - len(client_id_str)
        # Générer des chiffres aléatoires pour compléter le numéro
        random_digits = ''.join(random.choices("0123456789", k=num_random_digits))
        # Combiner le préfixe, l'ID du client, et les chiffres aléatoires pour former le numéro de carte complet
        card_number = prefix + client_id_str + random_digits
        return card_number
    
    def chargeHistorique(self):
        Historiques = get_all_history(self.code_user)
        layout = QVBoxLayout()
        if Historiques is not None:
            for histo in Historiques:
                win_orientation = QHBoxLayout()
                # Créer des QLabel pour chaque champ de l'historique
                transaction_type = QLabel(histo["transaction_type"])
                transaction_date = QLabel(histo["transaction_date"][:19].replace("T"," "))
                transaction_amount = QLabel(str(histo["transaction_amount"]))
                Emetteur = QLabel(str(histo["sender"]))
                Recepteur = QLabel(str(histo["receiver"]))
                frais = QLabel(str(histo["transaction_fee"]))
                win_orientation.addWidget(transaction_type)
                win_orientation.addWidget(transaction_date)
                win_orientation.addWidget(transaction_amount)
                win_orientation.addWidget(Emetteur)
                win_orientation.addWidget(Recepteur)
                win_orientation.addWidget(frais)
                win = QWidget()
                win.setLayout(win_orientation)
                win.setFixedHeight(50)
                win.setStyleSheet("background:red;margin-bottom:1px;border-radius:0px;")
                layout.addWidget(win)
        
        frame_tab = QWidget()
        frame_tab.setLayout(layout)
        return frame_tab
    
    
    def chargeHistorique2(self,vue):
        Historiques = get_all_history(self.code_user)
        layout = QVBoxLayout()
        if Historiques is not None: 
            for histo in Historiques:
                win_orientation = QHBoxLayout()
                # Créer des QLabel pour chaque champ de l'historique
                if histo["transaction_type"]==vue:
                    transaction_type = QLabel(histo["transaction_type"])
                    transaction_date = QLabel(histo["transaction_date"][:19].replace("T"," "))
                    transaction_amount = QLabel(str(histo["transaction_amount"]))
                    Emetteur = QLabel(str(histo["sender"]))
                    Recepteur = QLabel(str(histo["receiver"]))
                    frais = QLabel(str(histo["transaction_fee"]))
                    win_orientation.addWidget(transaction_type)
                    win_orientation.addWidget(transaction_date)
                    win_orientation.addWidget(transaction_amount)
                    win_orientation.addWidget(Emetteur)
                    win_orientation.addWidget(Recepteur)
                    win_orientation.addWidget(frais)
                    win = QWidget()
                    win.setLayout(win_orientation)
                    win.setFixedHeight(50)
                    win.setStyleSheet("background:red;margin-bottom:1px;border-radius:0px;")
                    layout.addWidget(win)
        frame_tab = QWidget()
        frame_tab.setLayout(layout)
        return frame_tab