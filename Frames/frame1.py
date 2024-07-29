from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import datetime
import locale
from settings import *
from operatings import *
import re

class History(QWidget):
    def __init__(self) -> None:
        super().__init__()


class Frame1(QWidget):
    def __init__(self,code_user) -> None:
        super().__init__()
        self.infoapk = commandes
        self.setStyleSheet("background-color:#2E2E2E;")
        self.setFixedSize(1200, 600)
        self.declaration(code_user)
        self.layout = QHBoxLayout()
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
        logo.setStyleSheet("background-color:blue;")
        
        name_logo = QLabel(str(self.infoapk["name_companie"]),w1)
        name_logo.setGeometry(55,8,150,25)
        name_logo.setStyleSheet("font-size:16px;font:bold;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        
        w1.setFixedHeight(40)
        w1.setStyleSheet("background-color:#2E2E2E;")
        w2 = QWidget()
        w2.setFixedHeight(40)
        w2.setStyleSheet("background-color:#2E2E2E;")
        layout2.addWidget(w1)
        layout2.addWidget(w2)

        box1.setLayout(layout2)
        box1.setFixedHeight(100)
        box1.setStyleSheet("background-color:yellow;")

        box2 = QWidget()
        box2.setFixedHeight(250)
        layout = QVBoxLayout()

        box3 = QWidget()
        bx3_layout =QVBoxLayout()


        self.b1 = QWidget()
        self.b1.setStyleSheet("background-color:#4BFFB3;")
        lb1_layout = QHBoxLayout()
        lb1 = QLabel("Acceuil")
        lb1.setStyleSheet("color:#808080;")
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
        lb2.setStyleSheet("color:#808080;")
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
        lb3.setStyleSheet("color:#808080;")
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
        lb4.setStyleSheet("color:#808080;")
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
        lb5.setStyleSheet("color:#808080;")
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
        lb6.setStyleSheet("color:#808080;")
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
        tit_hit.setStyleSheet("font-size:22px;font:bold;margin-left:10px;")
    
        choice_wid = QWidget()
        choice_wid.setFixedWidth(170)
        choice_lay = QHBoxLayout()

        alltext = QPushButton("All")
        depotext = QPushButton("Depot")
        retrait = QPushButton("Retrait")
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
        liste = ["Nature Transaction","Date Transaction","Solde Transaction","Emetteur","Recepteur","Methode Paiement","Pays Emission"]
        for i in liste:
            l = QLabel(i)
            l.setStyleSheet("font:bold;font-size:10px;")
            titles_layout.addWidget(l)
        titles_win.setLayout(titles_layout)
        titles_win.setGeometry(20,0,910,40)

        view_historique.setFixedHeight(380)
        History_scrolarea = QScrollArea(view_historique)
        frame_tab = QWidget()
        frame_tab_layout = QVBoxLayout()
        Historiques = get_all_historique(self.code_user)
        
        for histo in Historiques:
            win_orientation = QHBoxLayout()
             # Créer des QLabel pour chaque champ de l'historique
            Nature_Transaction = QLabel(histo["nature_transaction"])
            Date_Transaction = QLabel(histo["date_transaction"])
            Solde_Transaction = QLabel(str(histo["solde_transaction"]))
            Emetteur = QLabel(str(histo["emetteur_id"]))
            Recepteur = QLabel(str(histo["recepteur_id"]))
            Methode_Paiement = QLabel(histo["methode_paiement"])
            Pays_Emission = QLabel(histo["pays_emission"])
            
            win_orientation.addWidget(Nature_Transaction)
            win_orientation.addWidget(Date_Transaction)
            win_orientation.addWidget(Solde_Transaction)
            win_orientation.addWidget(Emetteur)
            win_orientation.addWidget(Recepteur)
            win_orientation.addWidget(Methode_Paiement)
            win_orientation.addWidget(Pays_Emission)
            win = QWidget()
            win.setLayout(win_orientation)
            win.setFixedHeight(50)
            win.setStyleSheet("background:red;margin-bottom:1px;border-radius:0px;")
            frame_tab_layout.addWidget(win)

        frame_tab.setLayout(frame_tab_layout)
        History_scrolarea.setWidget(frame_tab)
        History_scrolarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        History_scrolarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        History_scrolarea.setWidgetResizable(True)
        History_scrolarea.setGeometry(10,39,910,330)
        view_historique.setStyleSheet("background:#3D3D3D;border-radius:15px;")
        layout_transaction.addWidget(panel_top)
        layout_transaction.addWidget(tit_hit)
        layout_transaction.addWidget(choice_wid)
        layout_transaction.addWidget(view_historique)
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color: #2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)
    
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
        layout_transaction =QVBoxLayout()
        layout_transaction.addWidget(QWidget())
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color:#2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)
    
    def invoivepanel(self):
        # Sélectionner une option spécifique (assurez-vous que b2 est défini)
        self.selectionOption(self.b2)
        # Création du panel principal et des layouts
        panel_transaction = QWidget()
        layout_transaction = QHBoxLayout(panel_transaction)
        # Définir les listes pour les QComboBox
        nature_transaction_liste = ["Nature Transaction", "depot", "retrait"]
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
        dh_choice.setStyleSheet("background:transparent;font-size:10px;")
        fcfa_choice.setGeometry(100,17,100,20)
        fcfa_choice.setStyleSheet("background:transparent;font-size:10px;")
        groupRadio.setFixedHeight(250)
        groupRadio.setStyleSheet("background:transparent")
        
        
        
        # Créer le QGroupBox pour contenir les boutons radio
        groupRadio2 = QGroupBox("Status Frais Transaction/AM",three_frame_top)
        # Créer les QRadioButton pour les options de devises
        applique_choice = QRadioButton("Avec Frais",groupRadio2)
        noapplique_choice = QRadioButton("Sans Frais",groupRadio2)
        applique_choice.setStyleSheet("background:transparent;font-size:10px;")
        noapplique_choice.setStyleSheet("background:transparent;font-size:10px;")
        # Ajouter les QRadioButton au QGroupBox
        applique_choice.setChecked(True)
        applique_choice.setGeometry(5,17,100,20)
        noapplique_choice.setGeometry(95,17,100,20)
        groupRadio2.setFixedHeight(250)
        groupRadio2.setStyleSheet("background:transparent")
        
        
        
        
        nature_transaction = QComboBox(one_frame_top)
        nature_transaction.setFixedHeight(30)
        nature_transaction.setStyleSheet("background-color:#2E2E2E;border-radius:0px;")
        pays_emission = QComboBox(one_frame_top)
        pays_emission.setFixedHeight(30) 
        pays_emission.setStyleSheet("background-color:#2E2E2E;border-radius:0px;")
        methode_paiement = QComboBox(one_frame_top)
        methode_paiement.setFixedHeight(30)
        methode_paiement.setStyleSheet("background-color:#2E2E2E;border-radius:0px;")
        BP = QLabel(f"BP: {code_BP}",one_frame_top)
        BP.setStyleSheet("background:transparent")
        AG = QLabel(f"Agence: {AGENT}",one_frame_top)
        AG.setStyleSheet("background:transparent")
        
        nature_transaction.addItems(nature_transaction_liste)
        pays_emission.addItems(pays_emission_liste)
        methode_paiement.addItems(methode_paiement_liste )
        
        BP.setGeometry(12,5,100,30)
        AG.setGeometry(12,35,100,30)
        groupRadio.setGeometry(5,175,175,30)
        groupRadio2.setGeometry(5,175,175,30)
        nature_transaction.setGeometry(12,65,148,30)
        pays_emission.setGeometry(12,100,148,30)
        methode_paiement.setGeometry(12,135,148,30)
        
        
        
        two_frame_top = QWidget()
        two_frame_top_layout = QVBoxLayout()
        
        client_emetteur = QLabel("Emetteur Transaction")
        self.emetteur = QLineEdit()
        self.emetteur.setPlaceholderText("indicatif/telephone/nom emetteur")
        self.emetteur.setFixedHeight(30)
        self.emetteur.setStyleSheet("background-color:#2E2E2E;padding-left:12px;")
        client_recepteur = QLabel("Recepteur Transaction")
        self.recepteur =  QLineEdit()
        self.recepteur.setPlaceholderText("indicatif/telephone/nom recepteur")
        self.recepteur.setFixedHeight(30)
        self.recepteur.setStyleSheet("background-color:#2E2E2E;padding-left:12px;")
        client_solde = QLabel("Solde Transaction")
        self.solde =  QLineEdit()
        self.solde.setPlaceholderText("Montant de transaction")
        self.solde.setFixedHeight(30)
        self.solde.setStyleSheet("background-color:#2E2E2E;padding-left:12px;")
        
        code_Agent = QLabel(f"{AG_AM}")
        code_Agent.setStyleSheet("margin-left:50px;font-size:24px;")
        
        valide_transaction = QPushButton("Generer Facture")
        valide_transaction.setFixedHeight(30)
        valide_transaction.clicked.connect(self.clicked_genereted_facture)
        valide_transaction.setStyleSheet("background-color:green;")
        
        
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
        bottom_pan.setStyleSheet("background-color:#3D3D3D;border-radius:12px;")
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
        self.titlecomp.setStyleSheet("font-size:18px;font:bold;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        
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
        text_lab = QLabel("Generate Report")
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
        dh_solde,card_id = getsolde_dh(code)
        l2 = QLabel(f"{self.format_with_spaces(card_id,4)}",card)
        l3 = QLabel(f"MAD {dh_solde}",card)
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
        solde_fcfa,id_card= getsolde_fcfa(code);
        l2_2 = QLabel(self.format_with_spaces(id_card,4),card2)
        l3_3 = QLabel(f"FCFA {self.format_with_spaces(solde_fcfa,3)}",card2)
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

        historique_label = QLabel("Payment History",self.s2)
        historique_label.setGeometry(10,10,200,25)
        historique_label.setStyleSheet("font-size:18px;font:bold;color:#4BFFB3;")

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
        label_rescent = QLabel("Rescent transaction",s22)
        label_rescent.setStyleSheet("font-size:15px;font:bold;color:#4BFFB3;")
        label_rescent.setGeometry(10,10,150,20)

        frame_scroll = QScrollArea(s22)
        frame_rescent = QWidget()
        frame_layout = QVBoxLayout()
        Historiques = get_all_historique(self.code_user)
        deviseA, deviseB = "MAD", "FCFA"

        for elmt in Historiques:
            # Convertir en objet datetime
            datetime_obj = datetime.fromisoformat(elmt["date_transaction"])
            # Extraire la date uniquement
            date_only = datetime_obj.date()
            
            if date_only == datetime.now().date():
                t = QWidget()
                t_layout = QHBoxLayout()

                i = QLabel()
                i.setStyleSheet("background:#2E2E2E;border-radius:15px;")
                i.setAlignment(Qt.AlignCenter)
                i.setFixedSize(32, 32)

                j = QLabel()
                k = QLabel()

                if elmt["nature_transaction"] == "depot":
                    i.setPixmap(QPixmap(r"Frames\icons\190.png").scaled(20, 20))
                    j.setText("Depot")
                    k.setText(f"+{deviseA} {elmt['solde_transaction']}")
                elif elmt["nature_transaction"] == "retrait":
                    i.setPixmap(QPixmap(r"Frames\icons\17.png").scaled(20, 20))
                    j.setText("Retrait")
                    k.setText(f"-{deviseB} {elmt['solde_transaction']}")

                t_layout.addWidget(i)
                t_layout.addWidget(j)
                t_layout.addWidget(k)
                t.setLayout(t_layout)
                t.setFixedSize(160, 50)
                frame_layout.addWidget(t)
        
        frame_rescent.setLayout(frame_layout)
        frame_scroll.setWidget(frame_rescent)
        frame_scroll.setGeometry(0,30,181,200)
        frame_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        frame_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        frame_scroll.setWidgetResizable(True)
        
        s22.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")
        slayout2.addWidget(s12)
        slayout2.addWidget(s22)
        sous_panel_central_central_sous2.setLayout(slayout2)
        sous_panel_central_central_sous2.setStyleSheet("background-color:#2E2E2E")
        sous_panel_central_central_layout.addWidget(sous_panel_central_central_sous1)
        sous_panel_central_central_layout.addWidget(sous_panel_central_central_sous2)
        self.sous_panel_central_central.setLayout(sous_panel_central_central_layout)


    def defilementHistorique(self):
        self.s2 = QWidget()
        self.s2.setStyleSheet("background-color:#3D3D3D;border-radius:15px;")
        scroll = QScrollArea(self.s2)
        slide_historique = QWidget()
        slide_historique_layout = QVBoxLayout()
        Historiques = get_all_historique(self.code_user)
        if Historiques:  # Vérifier si la liste des historiques n'est pas vide
            for histo in Historiques:
                h1 = QWidget()
                icon = QLabel("")
                icon.setAlignment(Qt.AlignCenter)
                icon.setFixedSize(32,32)
                icon.setStyleSheet("background:#2E2E2E;border-radius:15px;border:transparent;")
                if histo["nature_transaction"] == "depot":
                    icon.setPixmap(QPixmap(r"Frames\icons\190.png").scaled(20,20))
                   
                if histo["nature_transaction"] == "retrait":
                    icon.setPixmap(QPixmap(r"Frames\icons\17.png").scaled(20,20))
                   
                # Assurez-vous que les clés existent et que les données sont correctement formatées
                emetteur_id = QLabel(str(histo.get("emetteur_id", "Inconnu")))
                emetteur_id.setStyleSheet("background-color:transparent;border:transparent;")
                date = QLabel(str(histo.get("date_transaction", "Date inconnue")))
                date.setStyleSheet("background-color:transparent;border:transparent;")
                argent = QLabel(str(histo.get("solde_transaction", "0.0")))
                argent.setStyleSheet("background-color:transparent;border:transparent;")
                nature = QLabel(histo.get("nature_transaction", "Nature inconnue"))
                nature.setStyleSheet("background-color:transparent;border:transparent;")
            
                
                layout_pan_histo = QHBoxLayout()
                layout_pan_histo.addWidget(icon)

                layout_pan_histo.addWidget(emetteur_id)
                layout_pan_histo.addWidget(date)
                layout_pan_histo.addWidget(argent)
                layout_pan_histo.addWidget(nature)

                h1.setStyleSheet("background-color:black;border-bottom:1px solid blue;border-radius:0px")
                h1.setFixedHeight(50)
                h1.setLayout(layout_pan_histo)
                slide_historique_layout.addWidget(h1)
            slide_historique.setLayout(slide_historique_layout)
            #Scroll Area Properties
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setWidgetResizable(True)
            scroll.setWidget(slide_historique)
            scroll.setGeometry(10,40,660,180)
    
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
                        
                        numero_facture=""
                        date= str(datetime.now())
                        emetteur_nom= nameE
                        emetteur_adresse=""
                        emetteur_recepteur=""
                        telephone_emetteur=phone_numberE
                        argent= self.solde.text().strip()+" "+devise
                        frais_argent=""
                        total_argent=""
                        net_recu = ""
                        client_nom = nameR
                        client_adresse = ""
                        client_email = ""
                        client_recepteur = phone_numberR
                        
                        
                        
                        self.update_facture(date_=date,emetteur_nom_=emetteur_nom,telephone_emetteur_=telephone_emetteur,
                                        argent_=argent,client_nom_=client_nom,client_recepteur_=client_recepteur)
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