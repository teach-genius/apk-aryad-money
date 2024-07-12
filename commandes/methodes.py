import requests
path = "http://127.0.0.1:8000/connexion" 
def call_api(name, psw):
    url = f"{path}/aryadmoney/{name}/{psw}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('connexion', False), response_json.get('code_user')
    else:
        return False, None