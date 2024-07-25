from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import requests
import datetime
import locale
import json

class History(QWidget):
    def __init__(self) -> None:
        super().__init__()


class Frame1(QWidget):
    def __init__(self,code_user) -> None:
        super().__init__()
        with open("parametre.json","r") as file:
            self.infoapk = json.load(file)
            file.close()
      
        self.setStyleSheet("background-color:#2E2E2E;")
        self.setFixedSize(1200, 600)

        self.declaration(code_user)
        self.layout = QHBoxLayout()
        self.lateral()
        self.central()

        self.setLayout(self.layout)
       
        
    
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
        date =datetime.date.today()
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
        for i in range(10):
            win = QWidget()
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
        self.selectionOption(self.b2)
        panel_transaction = QWidget()
        layout_transaction =QVBoxLayout()
        layout_transaction.addWidget(QWidget())
        panel_transaction.setLayout(layout_transaction)
        panel_transaction.setStyleSheet("background-color:#2E2E2E;")
        self.replace_widget(self.old_wid,panel_transaction)

    

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
        self.title = QLabel("AryadMoney")
        self.title.setStyleSheet("font-size:18px;font:bold;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        

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
        top_lauout.addWidget(self.title) 
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
        dh_solde,card_id = self.getsolde_dh(code)
        l2 = QLabel(f"{self.format_with_spaces(card_id)}",card)
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
        solde_fcfa,id_card= self.getsolde_fcfa(code);
        l2_2 = QLabel(self.format_with_spaces(id_card),card2)
        l3_3 = QLabel(f"FCFA {self.format_with_spaces3(solde_fcfa)}",card2)
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

        for i in range(100):
            t = QWidget()
            t_layout = QHBoxLayout()
            i = QLabel()
            i.setStyleSheet("background:#2E2E2E;border-radius:15px;")
            i.setPixmap(QPixmap(r"Frames\icons\17.png").scaled(20,20))
            i.setAlignment(Qt.AlignCenter)
            j = QLabel("Retrait")
            k = QLabel("-$265,00")       
            i.setFixedSize(32,32)
            t_layout.addWidget(i)
            t_layout.addWidget(j)
            t_layout.addWidget(k)
            t.setLayout(t_layout)
            t.setFixedSize(160,50)
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
        
        for i in range(20):
            h1 = QWidget()
            icon = QLabel("icon")
            name = QLabel("Name")
            date = QLabel("Date")
            argent = QLabel("Argent")
            card = QLabel("card")

            icon.setFixedSize(30,30)
            icon.setStyleSheet("background-color:red;border-radius:12px;")
            layout_pan_histo = QHBoxLayout()
            layout_pan_histo.addWidget(icon)

            layout_pan_histo.addWidget(name)
            layout_pan_histo.addWidget(date)
            layout_pan_histo.addWidget(argent)
            layout_pan_histo.addWidget(card)

            h1.setStyleSheet("background-color:black;border:1px solid blue;border-radius:0px")
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
    
    def format_with_spaces(self,number):
        # Convertir le nombre en chaîne de caractères s'il ne l'est pas déjà
        number_str = str(number)
        # Découper la chaîne en morceaux de 4 caractères
        chunks = [number_str[i:i+4] for i in range(0, len(number_str), 4)]
        # Joindre les morceaux avec un espace
        formatted_number = ' '.join(chunks)
        return formatted_number
    
    def format_with_spaces3(self,number):
        # Convertir le nombre en chaîne de caractères s'il ne l'est pas déjà
        number_str = str(number)
        # Découper la chaîne en morceaux de 4 caractères
        chunks = [number_str[i:i+3] for i in range(0, len(number_str), 3)]
        # Joindre les morceaux avec un espace
        formatted_number = ' '.join(chunks)
        return formatted_number
    
    def getsolde_fcfa(self,code_user):
        url = f"http://127.0.0.1:8000/solde_account/soldefcfa/aryadmoney/{code_user}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("solde_fcfa"),response.json().get("id_card")
        else:
            return False
    
    def getsolde_dh(self,code_user):
        url = f"http://127.0.0.1:8000/solde_account/soldedh/aryadmoney/{code_user}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("solde_dh"),response.json().get("id_card")
        else:
            return False
    
   