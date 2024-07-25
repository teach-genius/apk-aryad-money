from sqlalchemy import create_engine

path_db = "sqlite:///localdatabase.db"

engine = create_engine(path_db)


try:
    connect = engine.connect()
    print("success!")
except Exception as ex:
    print(ex)
