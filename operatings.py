from settings import URL_BASE
import requests

def create_user(name: str, firstname: str, country: str, phone: str, email: str, card_identity: str, city: str):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/USER"
    user_info = {
        "name": name,
        "firstname": firstname,
        "country": country,
        "phone": phone,
        "email": email,
        "card_identity": card_identity,
        "city": city
    }
    try:
        response = requests.post(url, json=user_info)
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return None

def get_all_users(id:int):
    url = f"{URL_BASE}/API/V1/ALL/USERS/EXISTS"
    user_info = {
        "id_user": id
    }
    try:
        response = requests.post(url, json=user_info)
        response.raise_for_status()
        return response.json().get("users")
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return None
    

def create_new_account_fcfa(balance: float, card: str, user_id: int, status: bool = False):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/ACCOUNT/FCFA"
    account_info = {
        "balance": balance,
        "card": card,
        "user_id": user_id,
        "status": status
    }
    try:
        response = requests.post(url, json=account_info)
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.RequestException as e:
        print(f"Error creating FCFA account: {e}")
        return None

def create_new_account_mad(balance: float, card: str, user_id: int, status: bool = False):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/ACCOUNT/MAD"
    account_info = {
        "balance": balance,
        "card": card,
        "user_id": user_id,
        "status": status
    }
    try:
        response = requests.post(url, json=account_info)
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.RequestException as e:
        print(f"Error creating MAD account: {e}")
        return None

def create_transaction_history(receiver: str, sender: str, transaction_amount: float, transaction_fee: float, transaction_type: str, receiver_id: int, sender_id: int):
    url = f"{URL_BASE}/API/V1/CREATE/TRANSACTION/HISTORY"
    transaction_info = {
        "receiver": receiver,
        "sender": sender,
        "transaction_amount": transaction_amount,
        "transaction_fee": transaction_fee,
        "transaction_type": transaction_type,
        "receiver_id": receiver_id,
        "sender_id": sender_id
    }
    try:
        response = requests.post(url, json=transaction_info)
        response.raise_for_status()
        return response.json().get("history")
    except requests.exceptions.RequestException as e:
        print(f"Error creating transaction history: {e}")
        return None

def create_security(username: str, password: str, user_type: str, activation_code: str, user_id: int, status: bool):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/SECURITY"
    security_info = {
        "username": username,
        "password": password,
        "user_type": user_type,
        "activation_code": activation_code,
        "user_id": user_id,
        "status": status
    }
    try:
        response = requests.post(url, json=security_info)
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

def get_id_user(name: str, firstname: str):
    url = f"{URL_BASE}/API/V1/GET/ID/USER"
    data = {
        "name": name,
        "firstname": firstname
    }
    try:
        response = requests.post(url, json=data)  # Changed to POST as per API definition
        response.raise_for_status()
        return response.json().get("id_user")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

def login(name: str, pswd: str):
    url = f"{URL_BASE}/API/V1/CHECK/USER/{name}/{pswd}/SECURITY"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("loginup")
    except requests.exceptions.RequestException as e:
        print(f"Login error: {e}")
        return None

def get_all_history(user_id: int):
    url = f"{URL_BASE}/API/V1/GET/ALL/{user_id}/HISTORIQUE"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("histories")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving history: {e}")
        return None

def get_balance_mad(user_id: int):
    url = f"{URL_BASE}/API/V1/GET/SOLDE/{user_id}/MAD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("account_info")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving MAD balance: {e}")
        return None

def get_balance_fcfa(user_id: int):
    url = f"{URL_BASE}/API/V1/GET/SOLDE/{user_id}/FCFA"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("account_info")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving FCFA balance: {e}")
        return None
