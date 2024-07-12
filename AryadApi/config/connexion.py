import psycopg2
from psycopg2 import sql

class Connexion:
    def __init__(self, db, user, pswd, host, port) -> None:
        self.__dbname = db
        self.__user = user
        self.__password = pswd
        self.__host = host
        self.__port = port

    def logindb(self):
        try:
            # Établir la connexion
            connection = psycopg2.connect(
                dbname=self.__dbname,
                user=self.__user,
                password=self.__password,
                host=self.__host,
                port=self.__port
            )
            return connection
        except Exception as error:
            print(f"Erreur lors de la connexion à la base de données : {error}")
            return None


