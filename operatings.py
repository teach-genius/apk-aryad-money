from settings import URL_BASE
import requests

def create_user(name: str, firstname: str, country: str, phone: str, email: str, card_identity: str, city: str) -> str:
    """
    Create a new user by sending a POST request to the API.

    Args:
        name (str): The name of the user.
        firstname (str): The first name of the user.
        country (str): The country of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
        card_identity (str): The identity card number of the user.
        city (str): The city of the user.

    Returns:
        str: A message indicating the success or failure of the user creation.
    """
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
        response.raise_for_status()  # Raises an error for HTTP error responses (4xx, 5xx)
        return response.json().get("message", "User created successfully.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    
    return "Failed to create user due to an error."


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

def create_new_account_mad_request(balance_, card_: str, user_id_: int, status_: bool):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/ACCOUNT/MAD"
    account_info = {
        "balance": balance_,
        "card": card_,
        "user_id": user_id_,
        "status": status_
    }
    try:
        response = requests.post(url, json=account_info)
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.RequestException as e:
        print(f"Error creating MAD account: {e}")
        return None


def create_transaction_history(receiver: str, sender: str, transaction_amount: float, transaction_fee: float, transaction_type: str, receiver_id: int, sender_id: int):
    url = f"{URL_BASE}/API/V1/CREATE/TRANSACTION/HISTORIQUE"
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
        return response.json().get("message")
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

def info_client(id_card: str):
    url = f"{URL_BASE}/API/V1/GET/INFO/CLIENT"
    try:
        info = {"id_card":id_card}
        response = requests.get(url,json=info)
        response.raise_for_status()
        return response.json().get("info_client")
    except requests.exceptions.RequestException as e:
        print(f"info client error: {e}")
        return None
def devise_client_account(name:str,firtsname:str):
    url = f"{URL_BASE}/API/V1/GET/INFO/CLIENT/DEVISE"
    try:
        info = {
            "name":name,
            "firstname":firtsname
        }
        response = requests.get(url,json=info)
        response.raise_for_status()
        return response.json().get("info")
    except requests.exceptions.RequestException as e:
        print(f"info client error: {e}")
        return None

def get_all_history(user_id: int):
    url = f"{URL_BASE}/API/V1/GET/ALL/{user_id}/HISTORIQUE"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("histories",None)
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

def create_recharge_card(user_id: int, numero: str, solde: float, card: str):
    url = f"{URL_BASE}/API/V1/CREATE/NEW/RECHARGE/CARD"
    data = {
        "user_id":user_id,
        "numero":numero,
        "solde":solde,
        "card":card
    }
    try:
        response = requests.post(url, json=data)  # Changed to POST as per API definition
        response.raise_for_status()
        return response.json().get("message")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None