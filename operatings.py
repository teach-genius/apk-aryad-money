from settings import URL_BASE
import requests
from datetime import datetime


class Compte:
    def __init__(self) -> None:
        # account fcfa
        self.Id_Fcfa_Card = None
        self.Solde_FCFA = None
        # account mad
        self.Solde_MAD = None
        self.Id_Mad_Card = None 
        # Historique
        self.Historique_transaction = None

def login(name, pswd):
    url = f"{URL_BASE}/login/myaccount/connect"
    data_login = {
        "user_name": name,
        "password":pswd
        }
    response = requests.post(url, json=data_login)
    return response.json().get("Token"),response.json().get("label")

def getsolde_dh(code:int):
    url = f"{URL_BASE}/mad_solde/myaccount/soldeaccount"
    data_solde = {
        "code":code
    }
    response = requests.post(url,json=data_solde)
    return response.json().get("solde"),response.json().get("id_card")

def getsolde_fcfa(code:int):
    url = f"{URL_BASE}/fcfa_solde/myaccount/soldeaccount"
    data_solde = {
        "code":code
    }
    response = requests.post(url,json=data_solde)
    return response.json().get("solde"),response.json().get("id_card")

def get_all_historique(code:int):
    url = f"{URL_BASE}/historique/myaccount/all"
    data_solde = {
        "code":code
    }
    response = requests.post(url,json=data_solde)
    return response.json().get("Historique",None)

def createsatususer(phone,email,cni,status):
    url = f"{URL_BASE}/type_user/myaccount/create"
    data_create = {
        "phone": phone,
        "email": email,
        "cni":cni,
        "status":status
    }
    response = requests.post(url, json=data_create)
    return response.json().get("Message", None)

def create_historique(nature_transaction: str, solde_transaction: float,  # type: ignore
                      emetteur_id: int, recepteur_id: int, methode_paiement: str, pays_emission: str):
    url = f"{URL_BASE}/create/historique/in_table_historique"
    
    # Utilise la date et l'heure actuelles pour la transaction
    date_transaction = datetime.now()
    
    db_historique = {
        "nature_transaction": nature_transaction,
        "date_transaction": date_transaction.isoformat(),  # Format ISO 8601
        "solde_transaction": solde_transaction,
        "emetteur_id": emetteur_id,
        "recepteur_id": recepteur_id,
        "methode_paiement": methode_paiement,
        "pays_emission": pays_emission
    }
    
  
    response = requests.post(url, json=db_historique)
    return response.json().get("Notification", None)



if __name__ == "__main__":
    
    b = get_all_historique(1)
    print(f"message : {b}")