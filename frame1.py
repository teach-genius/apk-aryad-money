from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class History(QWidget):
    def __init__(self) -> None:
        super().__init__()



class Frame1(QWidget):
    def __init__(self) -> None:
        super().__init__()
      
        self.setStyleSheet("background-color:#2E2E2E;")
        self.setFixedSize(1200, 600)

        self.declaration()
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

        b1 = QWidget()
        lb1_layout = QHBoxLayout()
        lb1 = QLabel("Acceuil")
        lb1.setStyleSheet("color:#808080;")
        ico_drach = QLabel()
        ico_drach.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon10.png").scaled(13,20))
        lb1_layout.addWidget(ico_drach)
        lb1_layout.addWidget(lb1)
        b1.setLayout(lb1_layout)
        b1.setFixedHeight(45)

        b2 = QWidget()
        lb2_layout = QHBoxLayout()
        lb2 = QLabel("Invoices")
        lb2.setStyleSheet("color:#808080;")
        ico_inv = QLabel()
        ico_inv.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon11.png").scaled(20,40))
        lb2_layout.addWidget(ico_inv)
        lb2_layout.addWidget(lb2)
        b2.setLayout(lb2_layout)
        b2.setFixedHeight(45)

        b3 = QWidget()
        lb3_layout = QHBoxLayout()
        lb3 = QLabel("Carte")
        lb3.setStyleSheet("color:#808080;")
        ico_card = QLabel()
        ico_card.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\19.png").scaled(30,30))
        lb3_layout.addWidget(ico_card)
        lb3_layout.addWidget(lb3)
        b3.setLayout(lb3_layout)
        b3.setFixedHeight(45)

        b4 = QWidget()
        lb4_layout = QHBoxLayout()
        lb4 = QLabel("Historique")
        lb4.setStyleSheet("color:#808080;")
        ico_history = QLabel()
        ico_history.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\20.png").scaled(30,30))
        lb4_layout.addWidget(ico_history)
        lb4_layout.addWidget(lb4)
        b4.setLayout(lb4_layout)
        b4.setFixedHeight(45)
        

        b5 = QWidget()
        lb5_layout = QHBoxLayout()
        lb5 = QLabel("Parametre")
        lb5.setStyleSheet("color:#808080;")
        ico_setting = QLabel()
        ico_setting.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon7.png").scaled(20,40))
        lb5_layout.addWidget(ico_setting)
        lb5_layout.addWidget(lb5)
        b5.setLayout(lb5_layout)
        b5.setFixedHeight(45)
       

        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(b3)
        layout.addWidget(b4)
        layout.addWidget(b5)
        box2.setLayout(layout)

        layout_btn.addWidget(box1)
        layout_btn.addWidget(box2)
        self.panel_lateral.setLayout(layout_btn)

        
        



    def central(self):
        panel_central = QWidget()
        panel_central_layout = QVBoxLayout()
        panel_central.setStyleSheet("background-color: #2E2E2E")
        panel_central_layout.addWidget(self.sous_panel_central_top)
        panel_central_layout.addWidget(self.sous_panel_central_central)
        panel_central.setLayout(panel_central_layout)
        self.layout.addWidget(panel_central)
    
    def declaration(self):
        self.title = QLabel("AryadMoney")
        self.title.setStyleSheet("font-size:18px;font:bold;color:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0#FFB74B,stop:1#32A528)")
        

        self.topcentralpan()
        self.centrepan()
       

    def topcentralpan(self):
        self.sous_panel_central_top = QWidget()
        self.sous_panel_central_top.setFixedHeight(60)

        w1 = QWidget()
        lay_out = QHBoxLayout()
        btn_search = QPushButton()
        barre_search = QLineEdit()
        barre_search.setPlaceholderText("Search")
        barre_search.setStyleSheet("color:black;")
        btn_search.setIcon(QIcon(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon5.png")))
        lay_out.addWidget(barre_search)
        lay_out.addWidget(btn_search)
        w1.setStyleSheet("background-color:#D9D9D9;border-radius:10px;")
        w1.setFixedSize(300,40)
        w1.setLayout(lay_out)

        w2 = QWidget()
        w2_layout = QHBoxLayout()
        w2.setFixedSize(100,40)
        b1 = QPushButton("")
        b1.setIcon(QIcon(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon1.png")))
        b1.setStyleSheet("background-color:transparent;")
        b1.setFixedSize(36,36)
        b2 = QPushButton("")
        b2.setIcon(QIcon(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\18.png")))
        b2.setStyleSheet("background-color:transparent;")
        b2.setFixedSize(36,36)
        b3 = QPushButton("")
        b3.setIcon(QIcon(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon3.png")))
        b3.setStyleSheet("background-color:transparent;")
        b3.setFixedSize(36,36)
        b4 = QPushButton("")
        b4.setIcon(QIcon(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon4.png")))
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
        lab_icon.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\icon6.png").scaled(16,16))
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
    
    def centrepan(self):
        self.sous_panel_central_central = QWidget()
        self.sous_panel_central_central.setStyleSheet("background-color:#2E2E2E")
        sous_panel_central_central_layout = QHBoxLayout()

        sous_panel_central_central_sous1 = QWidget()
        sous_panel_central_central_sous1.setFixedWidth(700)
        slayout = QVBoxLayout()
        
        s1 =QWidget()
        card = QWidget(s1)
        card.setStyleSheet("background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 1,  stop: 0 #284AA5, stop: 1 #4B7DFF);")

        l1 = QLabel("Current Balance",card)
        l2 = QLabel("5282 3456 7890 1289",card)
        l3 = QLabel("₹5,75,200",card)
        l4 = QLabel("09/25",card)

        l1.setGeometry(15,10,200,30)
        l1.setStyleSheet("font-size:15px;background:transparent;")

        l2.setGeometry(15,140,200,30)
        l2.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        l3.setGeometry(15,32,200,30)
        l3.setStyleSheet("font-size:30px;font:bold;background:transparent;")
        logo = QLabel(card)
        logo.setStyleSheet("background:transparent;")
        logo.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\13.png").scaled(43,27))
        logo.setGeometry(240,10,50,60)

        l4.setGeometry(235,140,40,20)
        l4.setStyleSheet("font-size:15px;font:bold;background:transparent;")

        
        card.setGeometry(10,13,300,178)
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
            i.setPixmap(QPixmap(r"C:\Users\farya\Desktop\AryadMoneyOriginal\projet\frames\icons\17.png").scaled(20,20))
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
  


