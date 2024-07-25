import psycopg2
from psycopg2 import sql
import json
class Connexion:
    def __init__(self) -> None:
        with open("parametre.json","r")as file:
            self.info = json.load(file)
            file.close()

    def logindb(self):
        try:
            # Établir la connexion
            connection = psycopg2.connect(
                dbname=self.info["db_name"],
                user=self.info["user_name"],
                password=self.info["password_db"],
                host=self.info["host"],
                port=self.info["port"]
            )
            return connection
        except Exception as error:
            print(f"Erreur lors de la connexion à la base de données : {error}")
            return None


