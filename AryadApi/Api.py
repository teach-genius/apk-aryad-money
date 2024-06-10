from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "index.html")) as f:
        return f.read()
    
@app.get("/services.html", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "services.html")) as f:
        return f.read()
    
@app.get("/contact.html", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "contact.html")) as f:
        return f.read()
    
@app.get("/about.html", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "about.html")) as f:
        return f.read()

@app.get("/index.html", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join("static", "index.html")) as f:
        return f.read()
    


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/connexion/{user_name}/{user_password}")
async def connected(user_name: str, user_password: str):
    if user_name == "farya" and user_password == "1705":
        return {"connexion": True}
    else:
        return {"connexion": False}

@app.get("/connexion/info_account/{user_id}")
async def user():
    info_account={
        "FCFA":"",
        "MAD":"",
        "Historique":[],
        "num_card_fcfa":88899900044,
        "num_card_mad":111222333444
    }
    return info_account