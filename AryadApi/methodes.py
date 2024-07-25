import string
import psycopg2
class Transaction:
    def __init__(self) -> None:
        self.date =None
        self.depart =None
        self.arrive = None
        self.solde =None
        
    def Retrait(self,id_cardA,id_cardB):
        
        if(True):
            """
            SELECT solde FROM COMPTE WHERE id_user = id_userA
            new_solde = old_solde-solde
            UPDATE TABLE COMPTE SET solde=str(new_solde) WHERE id_user =id_userA
            """
            return True
        else:
            return False
    
    def Depot(self,id_userA,solde):
        if(True):
            """
            SELECT solde FROM COMPTE WHERE id_user = id_userA
            new_solde = old_solde+solde
            UPDATE TABLE COMPTE SET solde=str(new_solde) WHERE id_user =id_userA
            """
            return True
        else:
            return False
        
    def ConsulterSolde(self,id_userA):
        requete = f"SELECT soldefcfa,soldemad FROM COMPTE WHERE id={id_userA}"
        return True
    
    def Transfer(self,id_userA,id_userB,solde):
        """
        Retrait(id_userA,solde)
        Depot(id_userB,solde)
        """
        return True
    
    def Notification(self,id_userA,id_userB):
        return True
    

