from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os
from config.connexion import Connexion

app = FastAPI()

def read_static_file(filename: str) -> str:
    filepath = os.path.join("static", filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Fichier '{filename}' non trouvé")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return read_static_file("index.html")

@app.get("/services.html", response_class=HTMLResponse)
async def read_services():
    return read_static_file("services.html")

@app.get("/contact.html", response_class=HTMLResponse)
async def read_contact():
    return read_static_file("contact.html")

@app.get("/about.html", response_class=HTMLResponse)
async def read_about():
    return read_static_file("about.html")

@app.get("/index.html", response_class=HTMLResponse)
async def read_index_html():
    return read_static_file("index.html")

@app.get("/connexion/{aryadmoney}/{user_name}/{user_password}")
async def connected(user_name: str, user_password: str, aryadmoney: str):
    client = Connexion(aryadmoney, "postgres", "uF4Xf^WQm(Yzm@ZXvJrh4NGw3g2GRQ", "localhost", "5432")
    connection = client.logindb()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SET search_path TO i_ope;
                SELECT code_user FROM tb_securite WHERE password = %s AND username = %s;
                """,
                (user_password, user_name)
            )
            result = cursor.fetchone()
        except Exception as error:
            print(f"Erreur lors de l'exécution de la requête : {error}")
            raise HTTPException(status_code=500, detail="Erreur interne du serveur")
        finally:
            cursor.close()
            connection.close()

        if result:
            return {"connexion": True, "code_user": result[0]}
        else:
            return {"connexion": False}
    else:
        raise HTTPException(status_code=500, detail="Connexion à la base de données échouée")

@app.get("/solde_account/soldefcfa/aryadmoney/{code_user}")
async def solde_fcfa_view(code_user: str):
    client = Connexion("aryadmoney", "postgres", "uF4Xf^WQm(Yzm@ZXvJrh4NGw3g2GRQ", "localhost", "5432")
    connection = client.logindb()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SET search_path TO i_ope;
                SELECT solde_fcfa, id_card FROM card_fcfa WHERE code_user = %s;
                """,
                (code_user,)
            )
            info = cursor.fetchone()
        except Exception as error:
            print(f"Erreur lors de l'exécution de la requête : {error}")
            raise HTTPException(status_code=500, detail="Erreur interne du serveur")
        finally:
            cursor.close()
            connection.close()

        if info:
            return {"solde_fcfa": info[0], "id_card": info[1]}
        else:
            raise HTTPException(status_code=404, detail="Informations de solde non trouvées")
    else:
        raise HTTPException(status_code=500, detail="Connexion à la base de données échouée")


@app.get("/solde_account/soldedh/aryadmoney/{code_user}")
async def solde_dh_view(code_user: str):
    client = Connexion("aryadmoney", "postgres", "uF4Xf^WQm(Yzm@ZXvJrh4NGw3g2GRQ", "localhost", "5432")
    connection = client.logindb()
    
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SET search_path TO i_ope;
                SELECT solde_dh, id_card FROM card_dh WHERE code_user = %s;
                """,
                (code_user,)
            )
            info = cursor.fetchone()
        except Exception as error:
            print(f"Erreur lors de l'exécution de la requête : {error}")
            raise HTTPException(status_code=500, detail="Erreur interne du serveur")
        finally:
            cursor.close()
            connection.close()

        if info:
            return {"solde_dh": info[0], "id_card": info[1]}
        else:
            raise HTTPException(status_code=404, detail="Informations de solde non trouvées")
    else:
        raise HTTPException(status_code=500, detail="Connexion à la base de données échouée")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
