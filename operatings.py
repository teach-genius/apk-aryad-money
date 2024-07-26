from settings import URL_BASE
import requests


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
    


if __name__ == "__main__":
    
    b = createsatususer("066251730","carineanganie@gmail.com","CNI00123","Agent_FL")
    print(f"message : {b}")
    
